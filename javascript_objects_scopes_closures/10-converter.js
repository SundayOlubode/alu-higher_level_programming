#!/usr/bin/node

const converter = (base) => {
  return (num = 0) => num.toString(base);
};

module.exports = { converter };
