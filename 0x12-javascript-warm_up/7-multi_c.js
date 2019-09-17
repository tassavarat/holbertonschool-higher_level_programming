#!/usr/bin/node

/* Prints "C is fun" x times */
if (!process.argv[2]) {
  console.log('Missing number of occurences');
} else if (process.argv[2] > 0) {
  for (let i = process.argv[2]; i; --i) {
    console.log('C is fun');
  }
}
