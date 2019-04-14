from django.shortcuts import render
from django.views.generic import ListView

from .models import Blog

# リストビュー　https://docs.djangoproject.com/ja/2.1/ref/class-based-views/generic-display/#listview
class BlogListView(ListView):
    model = Blog
