#!/usr/bin/node

/* Searches the second biggest int int list of arguments */
if (!process.argv[2] || process.argv.length === 3) {
  console.log('0');
} else {
  const l = Math.max.apply(Math, process.argv.slice(2));
  let sl = process.argv[2];

  for (let i = 3; process.argv[i]; ++i) {
    if (sl < process.argv[i] && process.argv[i] < l) {
      sl = process.argv[i];
    }
  }
  console.log(sl);
}
