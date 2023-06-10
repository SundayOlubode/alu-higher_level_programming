#!/usr/bin/node

exports.converter = (base) => {
  return (num = 0) => num.toString(base);
};
