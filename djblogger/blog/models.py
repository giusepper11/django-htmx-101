from django.db import models


class Post(models.Model):
    options = [
        ("draft", "Draft"),
        ("published", "Published"),
    ]

    title = models.CharField(max_length=100)
    subtitle = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, unique=True)
    author = models.ForeignKey(
        "auth.User", on_delete=models.CASCADE, related_name="posts"
    )
    content = models.TextField()
    status = models.CharField(max_length=10, choices=options, default="draft")
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)

    def __str__(self):
        return f"Title: {self.title} - Author: {self.author}"

    class Meta:
        ordering = [
            "-created_at",
        ]
        verbose_name = "Post"
        verbose_name_plural = "Posts"
