import requests
from django.shortcuts import render, redirect
from . import models
from . import spotify

# Create your views here.
def index(request):
    token = request.session.get('spotify_acesss_token')
    if token is None:
        return redirect('/music/login')

    albums = models.Album.objects.all()
    context = {
        'albums': albums,
        'spotify_access_token': token,
    }

    return render(request, 'music/index.html', context=context)

def todo(request):
    albums = models.Album.objects.filter(todo=True)
    context = {
        'albums': albums,
    }

    return render(request, 'music/index.html', context=context)

def login(request):
    client_id = spotify.CLIENT_ID 
    response_type = "code"
    redirect_uri = spotify.REDIRECT_URI 
    state = "whattf"
    scopes = [
        "playlist-modify-private",
        "user-read-currently-playing", 
        "user-modify-playback-state",
        "streaming",
        "playlist-read-private",
        "user-library-modify",
        "user-library-read",
        "user-read-playback-state",
        "playlist-modify-public",
    ]
    scopes_str = ' '.join(scopes)

    url = (
        f"{spotify.AUTH_URL}"
        f"?client_id={client_id}"
        f"&response_type={response_type}"
        f"&redirect_uri={redirect_uri}"
        f"&scope={scopes_str}"
        f"&state={state}"
    )
    return redirect(url, permanent=True)

def get_token(request):
    code = request.GET.get('code') 
    error = request.GET.get('error') 
    state = request.GET.get('state')
    
    payload = {
        "grant_type": "authorization_code",
        "code": code,
        "redirect_uri": spotify.REDIRECT_URI,
    }

    response = requests.post(
        spotify.TOKEN_URL, 
        auth=(spotify.CLIENT_ID, spotify.CLIENT_SECRET),
        data=payload,
    ).json()

    request.session['spotify_acesss_token'] = response['access_token']
    request.session['spotify_refresh_token'] = response['refresh_token']

    return redirect('/music')
