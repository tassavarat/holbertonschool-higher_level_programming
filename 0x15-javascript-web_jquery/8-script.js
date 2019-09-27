/* Fetches and lists all movies title */
$.get('https://swapi.co/api/films/?format=json', (r) => {
  for (const film of r.results) {
    $('#list_movies').append($('<li></li>').text(film.title));
  }
});
