from rest_framework import serializers

from .models import BlogPost, Author, Topic


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ["id", "name", "age"]


class TopicWithTopAuthorsSerializer(serializers.ModelSerializer):
    top_authors = serializers.SerializerMethodField()

    class Meta:
        model = Topic
        fields = ["id", "title", "top_authors"]

    def get_top_authors(self, obj):
        author_counts = {}
        for post in obj.prefetched_blog_posts:
            author_counts.setdefault(
                post.author.id,
                {
                    "name": post.author.name,
                    "age": post.author.age,
                    "post_count": post.author.blog_posts.count(),
                }
            )
        top_authors = sorted(
            author_counts.values(),
            key=lambda x: (x["post_count"], x["name"]),
            reverse=True
        )[:3]
        return top_authors


class BlogPostDetailSerializer(serializers.ModelSerializer):
    other_topics_by_author = serializers.SerializerMethodField()

    class Meta:
        model = BlogPost
        fields = [
            "id",
            "title",
            "content",
            "publication_date",
            "author",
            "topic",
            "other_topics_by_author",
        ]

    def get_other_topics_by_author(self, obj):
        return (
            obj.author.blog_posts
            .exclude(topic_id=obj.topic_id)
            .order_by("topic__title")
            .distinct()
            .values_list("topic__title", flat=True)
        )

    def to_representation(self, instance):
        repr = super().to_representation(instance)
        repr["topic"] = {
            "title": instance.topic.title
        }
        repr["author"] = {
            "name": instance.author.name,
            "age": instance.author.age,
        }
        return repr 
