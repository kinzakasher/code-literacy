var x = [],
  y = [],
  segNum = 2,
  segLength = 30;

for (var a = 0; a < segNum; a++) {
  x[a] = 0;
  y[a] = 0;
}

function setup() {
  createCanvas(400, 400);
  strokeWeight(15);
  stroke(200,255, 100);
}

function draw() {
  background(233,29,151);
  dragSegment(0, mouseX, mouseY);
  for( var a=0; a<x.length-1; a++) {
    dragSegment(a+1, x[a], y[a]);
  }
}

function dragSegment(a, xin, yin) {
  var dx = xin - x[a];
  var dy = yin - y[a];
  var angle = atan2(dy, dx);
  x[a] = xin - cos(angle) * segLength;
  y[a] = yin - sin(angle) * segLength;
  segment(x[a], y[a], angle);
}

function segment(x, y, a) {
  push();
  translate(x, y);
  line(0, 0, segLength, 0);
  pop();
}
