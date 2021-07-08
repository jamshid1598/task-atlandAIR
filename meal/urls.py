from django.urls import path
from .views import (
    HomeView,
    DetailView,
)


app_name='meal'


urlpatterns=[
    path('', HomeView.as_view(), name='home'),
    path('<slug:slug>/detail/', DetailView.as_view(), name='detail'),
]