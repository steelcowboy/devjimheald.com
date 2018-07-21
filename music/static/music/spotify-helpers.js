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

  $.ajax({
    type: "PUT",
    url: "https://api.spotify.com/v1/me/player/play",
    data: JSON.stringify(payload),
    contentType: "application/json",
    headers: {
        'Authorization': 'Bearer ' + TOKEN
    }
  });
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

