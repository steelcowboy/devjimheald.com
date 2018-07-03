from django.urls import path

from . import views

app_name = 'music'

urlpatterns = [
    path('', views.index, name='music-index'),
    path('todo', views.todo, name='music-todo'),
    path('login', views.login, name='music-login'),
    path('get_token', views.get_token, name='music-get-token'),
]
