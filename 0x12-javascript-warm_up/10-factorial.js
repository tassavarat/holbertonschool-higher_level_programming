#!/usr/bin/node

/* Computers and prints a factorial */
let n = parseInt(process.argv[2]);

for (let i = n - 1; i > 0; --i) {
  n *= i;
}
if (!n) {
  n = 1;
}
console.log(n);
