import random

from django.db import migrations
from faker import Faker


def create_sample_data(apps, schema_editor):
    fake = Faker()

    Author = apps.get_model("blog", "Author")
    Topic = apps.get_model("blog", "Topic")
    BlogPost = apps.get_model("blog", "BlogPost")    

    # DB clean up in first run
    Author.objects.all().delete()
    Topic.objects.all().delete()
    BlogPost.objects.all().delete()

    print("Creating authors...")
    authors = [
        Author.objects.create(name=fake.name(), age=random.randint(18, 60))
        for _ in range(300)
    ]

    print("Creating topics...")
    topics = topics = [
        Topic.objects.create(title=fake.sentence())
        for _ in range(7000)
    ]

    print("Creating blog posts...")
    for n in range(10000):
        if n % 1000 == 0:
            print(f"Creating blog post {n}/10000...")
        BlogPost.objects.create(
            title=fake.sentence(),
            content=fake.paragraph(),
            publication_date=fake.date_between(start_date="-2y", end_date="today"),
            author=random.choice(authors),
            topic=random.choice(topics),
        )

    print("Sample data creation complete.")


def delete_sample_data(apps, schema_editor):
    Author = apps.get_model("blog", "Author")
    Topic = apps.get_model("blog", "Topic")
    BlogPost = apps.get_model("blog", "BlogPost")
    BlogPost.objects.all().delete()
    Author.objects.all().delete()
    Topic.objects.all().delete()


class Migration(migrations.Migration):
    dependencies = [
        ("blog", "0001_initial"),
    ]

    operations = [
        migrations.RunPython(create_sample_data, delete_sample_data),
    ]
