from django.urls import re_path, path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('', views.BlogListCreate.as_view()),
    re_path(r'(?P<pk>[0-9]+)', views.BlogRetrieveUpdateDestroy.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
