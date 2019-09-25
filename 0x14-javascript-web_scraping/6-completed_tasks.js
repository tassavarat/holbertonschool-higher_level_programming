#!/usr/bin/node
/**
 * Computes number of tasks completed by user id
 * First argument is API URL
 */
const request = require('request');

const obj = {};

request.get(process.argv[2], function (err, resp, body) {
  if (err) console.log(err);
  else {
    for (const o of JSON.parse(body)) {
      if (o.completed) obj[o.userId] ? obj[o.userId]++ : obj[o.userId] = 1;
    }
    console.log(obj);
  }
});
