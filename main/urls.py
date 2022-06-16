from django.urls import path
from main.views import *

urlpatterns = [
    path('', HomeListView.as_view(), name='home'),

    path('post/<slug:slug>/', PostDetailView.as_view(), name='post_detail'),
    path('tag/<slug:slug>/', TagTemplateView.as_view(), name='tag'),
]
