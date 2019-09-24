#!/usr/bin/node
/**
 * Display status code of GET request
 * First arg is URL to request
 */
const request = require('request');

request.get(process.argv[2]).on('response', function (response) {
  console.log('code:', response.statusCode);
});
