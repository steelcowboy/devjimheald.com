from django.urls import path
from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('printable', views.PrintableView.as_view(), name='printable'),
    path('printable/<str:tag>', views.PrintableView.as_view(), name='printable_tagged'),
]
