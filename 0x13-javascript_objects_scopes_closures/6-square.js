#!/usr/bin/node
const pSquare = require('./5-square');

/**
 * Square class that defines square and inherits Rectangle of 5-square.js
 * Instance method charPrint(c) prints rectangle using 'C', 'X' if undefined
 */
module.exports = class Square extends pSquare {
  charPrint (C) {
    if (C == null) {
      super.print();
    } else {
      for (let i = 0; i < this.width; ++i) {
        console.log(C.repeat(this.width));
      }
    }
  }
};
