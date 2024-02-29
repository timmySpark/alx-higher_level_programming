// Fetches and lists the title of all movies using the url below

const url = 'https://swapi.co/api/films/?format=json';
$.get(url, function (data) {
  const films = data.results;
  for (const film of films) {
    $('ul#list_movies').append(`<li>${film.title}</li>`);
  }
});
