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
  let paused = false;

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

  player.on("ready", async ({ device_id }) => {
    setPlayer(device_id);
    let state = await waitUntilUserHasSelectedPlayer(player);
    paused = state.paused;
    toggleIcon(paused);
  });

  $("#search-form").submit(async function(event) {
    event.preventDefault();
    $("#searchResults").html("");
    let response = await search($("#query").val());
    buildResults(response);  
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
    console.log('Set to next track!');
  });

  $("#toggle").click(async function() {
    await player.togglePlay();
    paused = !paused;

    toggleIcon(paused);
  });

})();

