from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('printable', views.printable, name='printable'),
    path('printable/<str:tag>', views.printable, name='printable'),
]
