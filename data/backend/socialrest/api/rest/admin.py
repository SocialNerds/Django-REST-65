from django.contrib import admin
from .models import Blog, Category

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    pass

@admin.register(Category)
class BlogAdmin(admin.ModelAdmin):
    pass
