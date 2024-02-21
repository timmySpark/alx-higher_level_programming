#!/usr/bin/node
const request = require('request');
filename = process.argv[2];
request.get(filename).on('response', (response) =>
  console.log(`code: ${response.statusCode}`));
