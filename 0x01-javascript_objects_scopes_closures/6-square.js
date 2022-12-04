#!/usr/bin/node
const Rectangle = require('./4-rectangle');

class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    if (c) {
      for (let x = 0; x < parseInt(this.width); x++) {
        console.log(c.repeat(this.width));
      }
    } else {
      for (let x = 0; x < parseInt(this.width); x++) {
        console.log('X'.repeat(this.width));
      }
    }
  }
}

module.exports = Square;
