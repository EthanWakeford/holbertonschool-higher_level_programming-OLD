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

  rotate () {
    const temp = this.height;
    this.height = this.width;
    this.width = temp;
  }

  double () {
    this.height = this.height * 2;
    this.width = this.width * 2;
  }
}
module.exports = Rectangle;
