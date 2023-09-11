#!/usr/bin/node
let num = '';
if (process.argv.length > 2 && (typeof process.argv[2][0] !== 'undefined')) {
  num = process.argv[2][0].charCodeAt(0);
}
if (num >= 48 && num <= 57) {
  num = parseInt(process.argv[2]);
  for (let i = 0; i < num; i++) {
    console.log('C is fun');
  }
} else {
  console.log('Missing number of occurrences');
}
