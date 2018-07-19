function getAlbumHTML(album) {
  artist = album.artists[0].name;
  name = album.name;
  date = album.release_date;
  album_id = album.id;

  return `
    <h3 id="${album_id}" onclick="playAlbum(this.id)">${name}</h3>
    <span>
      <p>
        ${artist}
      </p>
      <p>
        ${date}
      </p>
    </span>
  `;
}

function playAlbum(id) {
  payload = {
    "context_uri": `spotify:album:${id}`,      
    "offset": {
      "position": 0
    }
  };
  console.log(payload);
}

function fetchTracks(albumId, callback) {
  $.ajax({
    url: 'https://api.spotify.com/v1/albums/' + albumId,
    headers: {
      'Authorization': 'Bearer ' + TOKEN
    },
    success: function (response) {
      callback(response);
    }
  });
};

function searchAlbums (query) {
  return new Promise(function(resolve, reject) {
    $.ajax({
      url: 'https://api.spotify.com/v1/search',
      headers: {
        'Authorization': 'Bearer ' + TOKEN
      },
      data: {
        q: query,
        type: 'album',
        limit: 10
      }
    })
    .done(function (response) {
      resolve(response.albums.items);
    }) 
    .fail(function (xhr) {
      console.log(xhr);
    });
  });
};

window.onSpotifyWebPlaybackSDKReady = () => {};

async function waitForSpotifyWebPlaybackSDKToLoad () {
  return new Promise(resolve => {
    if (window.Spotify) {
      resolve(window.Spotify);
    } else {
      window.onSpotifyWebPlaybackSDKReady = () => {
        resolve(window.Spotify);
      };
    }
  });
};

async function waitUntilUserHasSelectedPlayer (player) {
  return new Promise(resolve => {
    let interval = setInterval(async () => {
      let state = await player.getCurrentState();
      if (state !== null) {
        resolve(state);
        clearInterval(interval);
      }
    });
  });
};

(async () => {
  const { Player } = await waitForSpotifyWebPlaybackSDKToLoad();
  const token = TOKEN;
  const player = new Player({
    name: 'DevJim Music Manager',
    volume: 1.0,
    getOAuthToken: callback => { callback(token); }
  });

  player.on("player_state_changed", async () => {
    let state = await waitUntilUserHasSelectedPlayer(player);
    let {
      id,
      uri: track_uri,
      name: track_name,
      duration_ms,
      artists,
      album: {
        name: album_name,
        uri: album_uri,
        images: album_images
      }
    } = state.track_window.current_track;

    $("#thisiswhatsplaying").html(
      `You're listening to ${track_name} by ${artists[0].name}!`
    );
  });

  $("#search-form").submit(async function(event) {
    event.preventDefault();
    $("#searchResults").html("");
    let albums = await searchAlbums($("#query").val());
    $.each(albums, function (i, album) {
      html = getAlbumHTML(album);
      $("#searchResults").append(html);
    });
  });

  let connected = await player.connect();
  if (connected) {
    let state = await waitUntilUserHasSelectedPlayer(player);
    let {
      id,
      uri: track_uri,
      name: track_name,
      duration_ms,
      artists,
      album: {
        name: album_name,
        uri: album_uri,
        images: album_images
      }
    } = state.track_window.current_track;
    console.log(`You're listening to ${track_name} by ${artists[0].name}!`);
  }

  $("#prev").click(async function() {
    await player.previousTrack();
    console.log('Set to previous track!');
  });

  $("#next").click(async function() {
    await player.nextTrack();
    console.log('Set to previous next!');
  });

  $("#toggle").click(async function() {
    await player.togglePlay();
    console.log('Toggled playback!');
  });

})();

