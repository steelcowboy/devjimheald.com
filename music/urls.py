from django.urls import path

from . import views

app_name = 'music'

urlpatterns = [
    path('', views.index, name='index'),
    path('todo', views.todo, name='todo'),
]
