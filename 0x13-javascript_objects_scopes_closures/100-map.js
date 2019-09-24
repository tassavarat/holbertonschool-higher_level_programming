#!/usr/bin/node
/* Imports an array and computes new array */
const list = require('./100-data').list;

console.log(list);
console.log(list.map((v, i) => v * i));
