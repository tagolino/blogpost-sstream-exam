from django.db.models import Prefetch
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.views import APIView

from .models import Topic, BlogPost
from .pagination import BlogCustomPagination
from .serializers import TopicWithTopAuthorsSerializer, BlogPostDetailSerializer


class TopicListView(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = "blog/topic_list.html"

    pagination_class = BlogCustomPagination

    def get(self, request, format=None):
        queryset = (
            Topic.objects.prefetch_related(
                Prefetch(
                    "blog_posts",
                    queryset=BlogPost.objects.select_related("author").prefetch_related("author__blog_posts"),
                    to_attr="prefetched_blog_posts"
                )
            )
            .order_by("title")
        )

        if "title" in request.query_params:
            queryset = queryset.filter(title__icontains=request.query_params["title"])

        paginator = self.pagination_class()
        page = paginator.paginate_queryset(queryset, request)
        serializer = TopicWithTopAuthorsSerializer(page, many=True)
        return paginator.get_paginated_response({"topics": serializer.data})


class BlogPostListView(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = "blog/blogpost_list.html"

    pagination_class = BlogCustomPagination

    def get(self, request, format=None):
        queryset = (
            BlogPost.objects.all()
            .select_related("author", "topic")
            .prefetch_related("author__blog_posts")
            .order_by("title")
        )

        paginator = self.pagination_class()
        page = paginator.paginate_queryset(queryset, request, view=self)
        serializer = BlogPostDetailSerializer(page, many=True)
        return paginator.get_paginated_response({"blog_posts": serializer.data})
