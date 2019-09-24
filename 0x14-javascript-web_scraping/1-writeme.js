#!/usr/bin/node
/**
 * Writes string to file
 * First arg is file path
 * Second arg is string
 */
const fs = require('fs');

fs.writeFile(process.argv[2], process.argv[3], (err) => {
  if (err) console.log(err);
});
