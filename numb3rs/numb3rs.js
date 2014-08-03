var util = require('util');

var cache = [];
for (var i=0; i<100; i++) { cache[i] = []; }

var solv = function(matrix, _startPoint, _day, destPoint) {
  cache.forEach(function(arr) {
    for (var i=0; i < arr.length; i++) { arr[i] = -1; }
  });

  var search = function(startPoint, day) {
    if (cache[startPoint][day] > -1) { return cache[startPoint][day]; }
    if (day == 0) { return (destPoint == startPoint) ? 1 : 0; };

    var sum = 0;
    var arr = matrix[startPoint];
    for (var i=0; i < arr.length; i++) {
      var s = search(arr[i], day-1);
      sum += s / matrix[arr[i]].length;
    }

    return cache[startPoint][day] = sum;
  };

  return search(_startPoint, _day);
};

// parse -_-;;;;
var mode = {
  ready: "ready",
  desc: "desc", // read desc
  matrix: "matrix", // read matrix
  goal: "goal", // read goal
  solv: "solv" // read starts
};

var cm = mode.ready;
var toInt = function(s) { return parseInt(s); };
var nTimes, matrix, dest, day;
require('readline').createInterface({input: process.stdin, output: process.stdout, terminal: false})
  .on('line', function (cmd) {
    if (cm == mode.ready) {
      cm = mode.desc;
    } else if (cm == mode.desc) {
      var arr = cmd.split(' ').map(toInt);
      nTimes = arr[0];
      day = arr[1];
      dest = arr[2];
      matrix = [];
      cm = mode.matrix;
    } else if (cm == mode.matrix) {
      nTimes--;
      var mm = cmd.split(' ').map(toInt);
      var filtered = [];
      for (var i=0; i < mm.length; i++) {
        if (mm[i] != 0) { filtered.push(i); }
      }
      matrix.push(filtered.map(toInt));
      if (nTimes == 0) {
        cm = mode.goal;
      }
    } else if (cm == mode.goal) {
      // pass
      cm = mode.solv;
    } else if (cm == mode.solv) {
      var goals = cmd.split(' ').map(toInt);
      goals.forEach(function(point) {
        process.stdout.write(solv(matrix, point, day, dest).toFixed(8));
        process.stdout.write(" ");
      });
      cm = mode.desc;
      console.log("");
    }
  });
