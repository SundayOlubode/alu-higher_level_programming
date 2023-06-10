#!/usr/bin/node

const parentSquare = require('./5-square.js');

class Square extends parentSquare {
  constructor (size) {
    super(size);
  }

  charPrint (c) {
    let char = c;
    if (!c) {
      char = 'X';
    }
    for (let i = 0; i < this.size; i++) {
      console.log(char.repeat(this.size));
    }
  }
}

module.exports = Square;
