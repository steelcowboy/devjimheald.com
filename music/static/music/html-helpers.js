function toggleIcon(is_paused) {
  if (is_paused) {
    $("#toggle").removeClass("fa-pause-circle");
    $("#toggle").addClass("fa-play-circle");
  } else {
    $("#toggle").removeClass("fa-play-circle");
    $("#toggle").addClass("fa-pause-circle");
  }
};

function capitalizeFirstLetter(string) {
  return string.charAt(0).toUpperCase() + string.slice(1);
}

function getResultBlock(type, data) {
  let upper_type = capitalizeFirstLetter(type); 
  return `
  <div id="#${type}Results">
    <h2>
      ${upper_type} Results
    </h2>

    ${data}
  </div>
  `;
};

function addToResults(type, builder, items) { 
  let html = builder(items);
  $("#searchResults").append(getResultBlock(type, html));
};

function buildResults(search_response) {
  var header = `
    <h1>
      Search Results
    </h1>
  `;

  $("#searchResults").append(header);

  if (search_response.hasOwnProperty("artists")) { 
    addToResults("artist", getArtistsHTML, search_response.artists.items);
  }

  if (search_response.hasOwnProperty("albums")) { 
    addToResults("album", getAlbumsHTML, search_response.albums.items);
  }

  if (search_response.hasOwnProperty("tracks")) {
    addToResults("song", getSongsHTML, search_response.tracks.items);
  }
};

function getAlbumsHTML(albums) {
  var result = "";

  $.each(albums, function (i, album) {
    artist = album.artists[0].name;
    name = album.name;
    date = album.release_date;
    album_id = album.id;

    result = result.concat(`
     <h3 id="${album_id}" onclick="playAlbum(this.id)">${name}</h3>
     <span>
       <p>
         ${artist}
       </p>
       <p>
         ${date}
       </p>
     </span>
   `);
  });

  return result;
}

function getArtistsHTML(artists) {
  var result = "";

  $.each(artists, function (i, artist) {
    name = artist.name;
    artist_id = artist.id;

    result = result.concat(`
     <h3 id="${artist_id}" onclick="playArtist(this.id)">${name}</h3>
   `);
  });

  return result;
};

function getSongsHTML(tracks) {
  var result = "";

  $.each(tracks, function (i, track) {
    artist = track.artists[0].name;
    name = track.name;
    date = track.album.release_date;
    track_id = track.id;

    result = result.concat(`
     <h3 id="${track_id}" onclick="playSong(this.id)">${name}</h3>
     <span>
       <p>
         ${artist}
       </p>
       <p>
         ${date}
       </p>
     </span>
   `);
  });

  return result;
};
