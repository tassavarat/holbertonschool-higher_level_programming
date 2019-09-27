/* Fetches and replaces name of URL */
$.get('https://swapi.co/api/people/5/?format=json', (data) => {
  $('#character').text(data.name);
});
