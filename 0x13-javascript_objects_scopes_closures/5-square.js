#!/usr/bin/node
const Rectangle = require('./4-rectangle');

/**
 * Square class that defines square and inherits Rectangle of 4-rectangle.js
 */
class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }
}
module.exports = Square;
