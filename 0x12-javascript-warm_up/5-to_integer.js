#!/usr/bin/node
let num = '';
if (process.argv.length > 2) {
  num = process.argv[2][0].charCodeAt(0);
}
if (num >= 48 && num <= 57) {
  console.log('My number: ' + parseInt(process.argv[2]));
} else {
  console.log('Not a number');
}
