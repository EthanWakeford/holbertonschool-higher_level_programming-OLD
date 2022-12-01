#!/usr/bin/node
if (!process.argv[3]) {
  console.log(0);
} else {
  console.log(process.argv.slice(2).sort().reverse()[1]);
}
