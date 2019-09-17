#!/usr/bin/node

/* Prints number converted to integer, otherwise Not a number */
if (!parseInt(process.argv[2])) {
  console.log('Not a number');
} else {
  console.log('My number: %d', parseInt(process.argv[2]));
}
