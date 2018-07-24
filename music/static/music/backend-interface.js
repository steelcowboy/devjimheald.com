function submitMusicData(type, payload) {
  $.ajax({
    type: "POST",
    url: `/music/get_${type}`,
    data: JSON.stringify(payload),
    contentType: "application/json",
  });
};
