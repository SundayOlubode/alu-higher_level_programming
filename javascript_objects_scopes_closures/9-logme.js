#!/usr/bin/node

function logMe (item) {
  if (!this.count) this.count = 0;
  console.log(`${count}: ${item}`);
  this.count++;
}

module.exports = { logMe };
