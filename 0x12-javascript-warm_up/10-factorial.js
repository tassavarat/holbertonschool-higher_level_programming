#!/usr/bin/node

/* Computes and prints a factorial */
function factorial (n) {
  if (!n) {
    return 1;
  } else {
    return n * factorial(n - 1);
  }
}

console.log(factorial(parseInt(process.argv[2])));
