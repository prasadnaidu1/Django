from django.shortcuts import render
from django.views.generic import ListView

from .models import Article

class ViewAllArticle(ListView):
    model = Article
    template_name = "index.html"

