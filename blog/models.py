from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=100)
    age = models.PositiveIntegerField()

    def __str__(self):
        return self.name


class Topic(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    publication_date = models.DateField()
    author = models.ForeignKey(
        Author,
        null=True,
        on_delete=models.SET_NULL,
        related_name="blog_posts",
    )
    topic = models.ForeignKey(
        Topic,
        null=True,
        on_delete=models.SET_NULL,
        related_name="blog_posts",
    )

    def __str__(self):
        return self.title
