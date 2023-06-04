#!/usr/bin/node

const { argv } = require('node:process');

const argvLen = argv.length;

if (argvLen < 3) console.log('No argument');
if (argvLen === 3) console.log('Argument found');
if (argvLen > 3) console.log('Arguments found');
