from django.urls import path

from . import views

app_name = 'searchengine'

urlpatterns = [
    path('', views.search, name='search'),
]
