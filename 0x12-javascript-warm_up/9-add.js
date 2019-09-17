#!/usr/bin/node

/* Prints the addition of 2 integers */
function add (a, b) {
  return a + b;
}

console.log(add(parseInt(process.argv[2]), parseInt(process.argv[3])));
