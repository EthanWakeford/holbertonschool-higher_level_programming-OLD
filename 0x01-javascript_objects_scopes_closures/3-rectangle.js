#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (typeof w === 'number' && typeof h === 'number') {
      if (w > 0 && h > 0) {
        this.width = w;
        this.height = h;
      }
    }
  }

  print () {
    for (let x = 0; x < parseInt(this.height); x++) {
      console.log('X'.repeat(this.width));
    }
  }
}
module.exports = Rectangle;
