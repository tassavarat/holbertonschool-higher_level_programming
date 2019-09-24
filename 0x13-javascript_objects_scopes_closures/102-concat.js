#!/usr/bin/node
/* Concats 2 files */
const fs = require('fs');

let a = fs.readFileSync(process.argv[2]).toString();
a = a.concat(fs.readFileSync(process.argv[3]).toString());
fs.writeFile(process.argv[4], a, (err) => {
  if (err) throw err;
});
