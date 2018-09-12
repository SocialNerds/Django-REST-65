from rest_framework import generics, mixins
from .models import Blog
from .serializers import BlogSerializer
from django_filters.rest_framework import DjangoFilterBackend


class BlogListCreate(generics.ListCreateAPIView):
    """
    List all, create.
    """
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('title', 'body', 'categories', 'author', 'published')

class BlogRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update or delete specific.
    """
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
