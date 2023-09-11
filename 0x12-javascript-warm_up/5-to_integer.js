#!/usr/bin/node
let num = '';
if (process.argv.length > 2 && (typeof process.argv[2][0] !== 'undefined')) {
  num = process.argv[2][0].charCodeAt(0);
}
if (num >= 48 && num <= 57) {
  console.log('My number: ' + parseInt(process.argv[2]));
} else if (num === 45) {
  process.exit(0);
} else {
  console.log('Not a number');
}
