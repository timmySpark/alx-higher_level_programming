#!/usr/bin/node
const request = require('request');
filename = process.argv[2];
request.get(process.argv[2]).on('response', (response) =>
  console.log(`code: ${response.statusCode}`));
