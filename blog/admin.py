from django.contrib import admin

from .models import Author, Topic, BlogPost


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ("name", "age")
    search_fields = ("name",)


@admin.register(Topic)
class TopicAdmin(admin.ModelAdmin):
    list_display = ("title",)
    search_fields = ("title",)


@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "topic", "publication_date")
    list_filter = ("topic", "author", "publication_date")
    search_fields = ("title", "content")
