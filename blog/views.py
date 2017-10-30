from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse(f"Welcome to my blog, {request.META['REMOTE_ADDR']}")
