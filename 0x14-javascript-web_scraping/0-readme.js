#!/usr/bin/node
/**
 * Reads and prints contents of a file */

const fs = require('fs');

fs.readFile(process.argv[2], function (err, data) {
  if (err) console.log(err);
  else process.stdout.write(data);
});
