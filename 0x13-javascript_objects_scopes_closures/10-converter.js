#!/usr/bin/node

/**
 * converter - Converts number from base 10 to specified base
 * @base: Base to convert to
 *
 * Return: Converted number
 */
exports.converter = function (base) {
  return function (n) {
    return (n.toString(base));
  };
};
