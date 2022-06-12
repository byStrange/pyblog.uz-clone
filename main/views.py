from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from main.models import *

# Create your views here.

class HomeListView(TemplateView):
    template_name = "index.html"
