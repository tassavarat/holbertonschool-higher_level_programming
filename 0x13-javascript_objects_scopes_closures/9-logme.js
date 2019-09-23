#!/usr/bin/node

let count = 0;
/**
 * Prints number of arguments already printed and the new argument value
 */
exports.logMe = function (item) {
  console.log('%d: %s', count, item);
  ++count;
};
