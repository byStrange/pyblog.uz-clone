from django.urls import path
from main.views import *

urlpatterns = [
    path('', HomeListView.as_view(), name='home'),
]
