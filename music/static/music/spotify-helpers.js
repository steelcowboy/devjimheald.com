function play(payload) {
  $.ajax({
    type: "PUT",
    url: "https://api.spotify.com/v1/me/player/play",
    data: JSON.stringify(payload),
    contentType: "application/json",
    headers: {
        'Authorization': 'Bearer ' + TOKEN
    }
  });
};

function playAlbum(id) {
  payload = {
    "context_uri": `spotify:album:${id}`,      
    "offset": {
      "position": 0
    }
  };

  play(payload);
};

function playArtist(id) {
  payload = {
    "context_uri": `spotify:artist:${id}`,      
  };

  play(payload);
};

function playSong(id) {
  payload = {
    "uris": [`spotify:track:${id}`],      
  };

  play(payload);
};

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

function search (query) {
  query_comp = query.split(" ")

  var def_type = "album,artist,track";
  var new_type = null;
  var type = null;

  // Bangs in search to select a type
  switch (query_comp[0]) {
    case "!al":
      new_type = "album";
      break;
    case "!ar":
      new_type = "artist";
      break;
    case "!s":
      new_type = "track";
      break;
  }

  // If we used a bang, remove it from the query. Otherwise fall back to the default
  if (new_type != null) {
    query = query_comp.slice(1).join(" ");
    type = new_type;
  }
  else {
    type = def_type;
  }
  
  data = {
    q: query,
    type: type,
    limit: 10,
  };
  console.log(data);
  
  return new Promise(function(resolve, reject) {
    $.ajax({
      url: 'https://api.spotify.com/v1/search',
      headers: {
        'Authorization': 'Bearer ' + TOKEN
      },
      data: data, 
    })
    .done(function (response) {
      console.log(response);
      resolve(response);
    }) 
    .fail(function (xhr) {
      console.log(xhr);
    });
  });
};

function setPlayer(device_id) {
  payload = {
    device_ids: [device_id],
  };

  $.ajax({
    type: "PUT",
    url: "https://api.spotify.com/v1/me/player",
    data: JSON.stringify(payload),
    contentType: "application/json",
    headers: {
        'Authorization': 'Bearer ' + TOKEN
    }
  })
  .fail(function (xhr) {
    console.log(xhr);
  });
};
