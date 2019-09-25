#!/usr/bin/node
/**
 * Prints all characters of specified Star Wars movie
 * First argument is Movie ID
 */
const request = require('request');

request(`https://swapi.co/api/films/${process.argv[2]}/`,
  function (err, resp, body) {
    if (err) console.log(err);
    else {
      for (const i of JSON.parse(body).characters) {
        request(i, function (err, resp, body) {
          if (err) console.log(err);
          else console.log(JSON.parse(body).name);
        });
      }
    }
  });
