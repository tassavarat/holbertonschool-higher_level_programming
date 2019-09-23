#!/usr/bin/node
/**
 * Creates a class Rectangle that defines a rectangle
 * Uses class notation
 * Takes 2 arguments
 * Initialises width and height to w and h respectively
 * Creates empty object if either w or h is 0 or negative
 * Has instance method that prints rectangle using 'X'
 */
module.exports = class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let i = 0; i < this.height; ++i) {
      console.log('X'.repeat(this.width));
    }
  }
};
