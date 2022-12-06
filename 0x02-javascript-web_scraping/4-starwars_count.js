#!/usr/bin/node
const request = require('request');

const url = process.argv[2];
const wedgeId = 'https://swapi-api.hbtn.io/api/people/18/';

request(url, (error, response, body) => {
  if (error) throw error;
  let antillesCount = 0;
  for (const movie of ((JSON.parse(body)).results)) {
    if (movie.characters.includes(wedgeId)) {
      antillesCount++;
    }
  }
  console.log(antillesCount);
});
