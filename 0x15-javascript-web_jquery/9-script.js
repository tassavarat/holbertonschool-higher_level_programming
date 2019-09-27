/* Fetches from URL and displays value of hello from fetch in DIV#hello */
$.ajax({
  type: 'GET',
  url: 'https://fourtonfish.com/hellosalut/?lang=fr',
  success: (r) => {
    $('#hello').text(r.hello);
  }
});
