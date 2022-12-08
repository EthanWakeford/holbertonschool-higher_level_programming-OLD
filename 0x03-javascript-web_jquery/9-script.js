const url = 'https://stefanbohacek.com/hellosalut/?lang=fr';
$.get(url, function (data) {
  $('DIV#hello').text(data.hello);
});
