# Optimize Blog Post Retrieval (Django App)

A Django project for getting blog posts, topics, and authors.

- Blog Post and Topic models with Author relations
- Topic search with top 3 authors by blog post count (per topic)
- Blog post list showing related topics the author has written about
- Optimized database queries using:
  - `select_related` for foreign keys
  - `prefetch_related` for reverse relationships
  - `annotate` for counting blog posts
- DB: SQLite
---

# Setup

### 1. Clone the Repository

```bash
$ git clone https://github.com/tagolino/blogpost-sstream-exam.git
$ cd your-django-blog-project
```

### 2. Create and Activate a Virtual Environment
```bash
$ python -m venv venv
$ source venv/bin/activate
# Windows: venv\Scripts\activate
```

### 3. Install Dependencies
```bash
$ pip install -r requirements.txt
```

### 4. Run Migrations
```bash
$ python manage.py makemigrations
$ python manage.py migrate
```

### 5. Create Superuser (Optional but Recommended)
```bash
$ python manage.py createsuperuser
```

### 6. Run the Development Server
```bash
$ python manage.py runserver
```
