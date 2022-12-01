#!/usr/bin/node
if (!parseInt(process.argv[3])) {
  console.log(0);
} else {
  console.log(process.argv.slice(2).sort()[1]);
}
