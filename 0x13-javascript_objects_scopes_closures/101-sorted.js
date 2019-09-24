#!/usr/bin/node
/* Computes a dictionary of user ids by occurences */
const dict = require('./101-data').dict;

const obj = {};

for (const v of Object.values(dict)) {
  const list = [];
  obj[v] = list;

  for (const [ke, va] of Object.entries(dict)) {
    if (v === va) {
      list.push(ke);
    }
  }
}
console.log(obj);
