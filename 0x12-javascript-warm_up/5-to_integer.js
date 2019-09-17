#!/usr/bin/node

/* Prints number converted to integer, otherwise Not a number */
if (!parseInt(process.argv[2])) {
  console.log('Not a number');
} else {
  console.log(parseInt(process.argv[2]));
}
