from django.shortcuts import render
from django.views.generic import ListView

from .models import Article

class ViewAllArticles(ListView):
    model =  Article
