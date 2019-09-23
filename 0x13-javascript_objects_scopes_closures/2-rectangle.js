#!/usr/bin/node
/**
 * Creates a class Rectangle that defines a rectangle
 * Creates an empty object if w or h is 0 or negative integer
 */
module.exports = class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }
};
