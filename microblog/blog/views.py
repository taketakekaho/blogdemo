from django.shortcuts import render
from django.views.generic import ListView

from .models import Blog
from django.views.generic import DetailView

# リストビュー　https://docs.djangoproject.com/ja/2.1/ref/class-based-views/generic-display/#listview
class BlogListView(ListView):
    model = Blog

# ディテールビュー　https://docs.djangoproject.com/ja/2.1/ref/class-based-views/generic-display/#detailview
class BlogDetailView(DetailView):
    model = Blog