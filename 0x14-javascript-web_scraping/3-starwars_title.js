#!/usr/bin/node
/**
 * Prints title of a Star Wars movie where number matches given integer
 * First arg is episode number
 */
const request = require('request');

request.get(`https://swapi.co/api/films/${process.argv[2]}/`,
  function (error, response, body) {
    if (error) console.log(error);
    else console.log(JSON.parse(body).title);
  });
