#!/usr/bin/node

/**
 * nbOccurences - Counts specified occurences in a list
 * @list: Array of data
 * @searchElement: Element being counted
 *
 * Return: Number of occurences
 */
exports.nbOccurences = function (list, searchElement) {
  let count = 0;

  for (let i = 0; i < list.length; ++i) {
    if (list[i] === searchElement) {
      ++count;
    }
  }
  return (count);
};
