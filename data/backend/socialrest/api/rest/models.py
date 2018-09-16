from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    """ The category of the blog post item """

    # Category title.
    title = models.CharField(
        max_length=60,
        verbose_name="Title",
        help_text="The title of the category.",
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Categories"

class Blog(models.Model):
    """ The blog post item """

    # Title.
    title = models.CharField(
        max_length=60, 
        verbose_name="Title",
        help_text="The title of the blog post.",
        null=False, # By default is not null.
    )

    # Text.
    body = models.TextField(
        max_length=8000,
        verbose_name="Body",
        help_text="The body of the blog post.",
    )

    # Timestamp of creation date.
    created = models.DateTimeField(
        auto_now_add=True
    )

    # If blog post is published. 
    published = models.BooleanField(
        default=False,
        verbose_name="Published",
        help_text="If blog post is published.",
    )

    # Categories.
    categories = models.ManyToManyField(
        Category,
        verbose_name="Categories",
        help_text="The categories of this blog post.",
    )

    # Author
    author = models.ForeignKey(
        User,
        models.SET_NULL,
        verbose_name="Author",
        help_text="The author of this blog post.",
        blank=True,
        null=True,
    )

    def __str__(self):
        return self.title
