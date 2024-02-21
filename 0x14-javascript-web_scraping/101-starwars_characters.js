#!/usr/bin/node
// script that prints all chars of a Star Wars movie.
const request = require('request');
const url = 'https://swapi-api.alx-tools.com/api/films/' + process.argv[2];
request(url, (error, response, body) => {
  if (!error) {
    const chars = JSON.parse(body).characters;
    printchar(chars, 0);
  }
});

function printchar (chars, index) {
  request(chars[index], (error, response, body) => {
    if (!error) {
      console.log(JSON.parse(body).name);
      if (index + 1 < chars.length) {
        printchar(chars, index + 1);
      }
    }
  });
}
