from statistics import mode
from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from . import models

# Create your views here.


class HomeListView(ListView):
    model = models.Post
    template_name = "index.html"


class PostDetailView(DetailView):
    model = models.Post
    template_name = "details.html"


class TagTemplateView(TemplateView):
    template_name = "tag.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        tag = self.kwargs.get('slug')
        context['tag'] = tag
        context['posts'] = models.Post.objects.filter(tags__name__iexact=tag)
        return context
