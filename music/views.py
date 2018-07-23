import requests
from datetime import datetime, timedelta

from django.shortcuts import render, redirect
from django.http import HttpResponse
from . import models
from . import spotify

# Create your views here.
def index(request):
    token = request.session.get('spotify_acesss_token')

    if token is None:
        return redirect('/music/login')

    if request.session.get_expiry_age() <= 0: 
        return redirect('/music/get_token')
    
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
        # Required scopes
        "streaming",
        "user-read-birthdate",
        "user-read-email",
        "user-read-private", 

        # For the endpoints I want
        "user-read-currently-playing", 
        "user-library-read",
        "user-library-modify",
        "user-read-playback-state",
        "user-modify-playback-state",
        "playlist-read-private",
        "playlist-modify-private",
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
    
    refresh_token = request.session.get("spotify_refresh_token")

    # If there is no refresh token, the client SHOULD have sent a code from /login
    if refresh_token is None:
        if error is not None:
            return HttpResponse(
                "Error logging in: {error}. Please go back and try again",
                status=401
            )

        if code is None:
            return HttpResponse(
                "No code provided, did you login first?",
                status=400
            )
    # Otherwise just use the refresh token as the code
    else:
        code = refresh_token if code is None else code

    print(f"Using code {code}")
    
    payload = {
        "grant_type": "authorization_code",
        "code": code,
        "redirect_uri": spotify.REDIRECT_URI,
    }

    response = requests.post(
        spotify.TOKEN_URL, 
        auth=(spotify.CLIENT_ID, spotify.CLIENT_SECRET),
        data=payload,
    )
    
    resp_json = response.json()
    
    if response.status_code != 200:
        return HttpResponse(
            f"Error getting token from Spotify: {resp_json}",
            status=response.status_code,
        )

    request.session['spotify_acesss_token'] = resp_json['access_token']
    request.session['spotify_refresh_token'] = resp_json['refresh_token']
    print(f"Will expire in {int(resp_json['expires_in'])}")
    request.session.set_expiry(int(resp_json['expires_in']))

    return redirect('/music')
