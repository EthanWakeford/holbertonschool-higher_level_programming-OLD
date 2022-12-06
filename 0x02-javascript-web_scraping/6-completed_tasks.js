#!/usr/bin/node
const request = require('request');

const url = process.argv[2];

request(url, 'utf8', (err, response, body) => {
  if (err) throw err;
  const completedTasks = {};
  for (const task of JSON.parse(body)) {
    if (task.completed === true) {
      if (task.userId in completedTasks) {
        completedTasks[(task.userId)]++;
      } else {
        completedTasks[(task.userId)] = 1;
      }
    }
  }
  console.log(completedTasks);
});
