from django.shortcuts import render
from . import models

# Create your views here.
def index(request):
    albums = models.Album.objects.all()
    context = {
        'albums': albums,
    }

    return render(request, 'music/index.html', context=context)
