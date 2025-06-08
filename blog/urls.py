from django.urls import path

from .views import TopicListView, BlogPostListView


urlpatterns = [
    path("topics/", TopicListView.as_view(), name="topic-list"),
    path("posts/", BlogPostListView.as_view(), name="blogpost-list"),
]
