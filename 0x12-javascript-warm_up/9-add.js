#!/usr/bin/node
let num = '';
let num2 = '';
if (process.argv.length > 3 && (typeof process.argv[2][0] !== 'undefined')) {
  num = process.argv[2][0].charCodeAt(0);
}
if (num >= 48 && num <= 57 && (typeof process.argv[3][0] !== 'undefined')) {
  num = process.argv[3][0].charCodeAt(0);
  if (num >= 48 && num <= 57) {
    num = parseInt(process.argv[2]);
    num2 = parseInt(process.argv[3]);
    console.log(add(num, num2));
  }
} else if (num === 45) {
  process.exit(0);
} else {
  console.log('Nan');
}

function add (a, b) {
  return (a + b);
}
