from django.shortcuts import render
from django.views.generic import TemplateView, ListView, CreateView
from posts.models import Post
from django import forms


class IndexView(ListView):
    template_name = 'index.html'
    model = Post
    context_object_name = 'posts'

