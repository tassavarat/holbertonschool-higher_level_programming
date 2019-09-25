#!/usr/bin/node
/**
 * Computes number of tasks completed by user id
 * First argument is API URL
 */
const request = require('request');

const obj = {};
let count = 0;

request.get(process.argv[2], function (err, resp, body) {
  if (err) console.log(err);
  else {
    for (const i of JSON.parse(body)) {
      obj[i.userId] = count;
      count = 0;
      for (const j of JSON.parse(body)) {
        if (j.userId === i.userId && j.completed === true) ++count;
      }
    }
    console.log(obj);
  }
});
