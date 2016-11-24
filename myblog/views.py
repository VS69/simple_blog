# coding: utf-8

from django.views.generic import ListView, DetailView

from myblog.models import Post


# Представлення у вигляді списку
class PostsListView(ListView):
    model = Post


# Деталізоване представлення
class PostDetailView(DetailView):
    model = Post
