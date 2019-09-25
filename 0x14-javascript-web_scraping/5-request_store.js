#!/usr/bin/node
/**
 * Gets contents of webpage and stores in file
 * First argument is URL to request
 * Second argument is path to store body response
 */
const request = require('request');
const fs = require('fs');

request.get(process.argv[2], function (error, response, body) {
  if (error) console.log(error);
  else {
    fs.writeFile(process.argv[3], body, (err) => {
      if (err) console.log(err);
    });
  }
});
