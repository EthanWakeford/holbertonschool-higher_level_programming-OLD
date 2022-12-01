#!/usr/bin/node
if (!parseInt(process.argv[2])) {
  console.log('Missing number of occurrences');
} else {
  for (let x = 0; x < parseInt(process.argv[2]); x++) {
    console.log('X'.repeat(process.argv[2]));
  }
}
