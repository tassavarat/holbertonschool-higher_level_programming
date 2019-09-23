#!/usr/bin/node
const Rectangle = require('./5-square');

/**
 * Square class that defines square and inherits Rectangle of 5-square.js
 * Instance method charPrint(c) prints rectangle using 'C', 'X' if undefined
 */
class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }

  charPrint (C) {
    if (C === undefined) {
      super.print();
    } else {
      for (let i = 0; i < this.width; ++i) {
        console.log('C'.repeat(this.width));
      }
    }
  }
}
module.exports = Square;
