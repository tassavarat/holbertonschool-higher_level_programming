#!/usr/bin/node

/* Prints two arguments passed with is in between */
if (!process.argv[2]) {
  console.log('undefined is undefined');
} else {
  console.log(process.argv[2].concat(' is ', process.argv[3]));
}
