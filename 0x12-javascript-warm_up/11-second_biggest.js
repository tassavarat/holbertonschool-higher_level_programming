#!/usr/bin/node

/* Searches the second biggest int int list of arguments */
if (process.argv.length === 2 || process.argv.length === 3) {
  console.log('0');
} else {
  const l = Math.max.apply(null, process.argv.slice(2));
  let sl;
  if (process.argv[2] !== l) {
    sl = parseInt(process.argv[2]);
  } else {
    sl = parseInt(process.argv[3]);
  }

  for (let i = 3; process.argv[i]; ++i) {
    if (sl < process.argv[i] && process.argv[i] < l) {
      sl = process.argv[i];
    }
  }
  console.log(String(sl));
}
