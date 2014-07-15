function solv(arr) {
  var fence = function(i, j) {
    if (j-i == 0) { return arr[i]; };
    var mid = Math.floor((j+i) / 2);
    var max = Math.max(fence(i, mid), fence(mid+1, j));

    // merge
    var left = mid, right = mid;
    var height = Math.min(arr[left], arr[right]);

    while (left > i || right < j) {
      if (right < j && arr[right+1] > arr[left-1] || left == i) {
        right++;
        height = Math.min(height, arr[right]);
      } else {
        left--;
        height = Math.min(height, arr[left]);
      }
      max = Math.max(max, (right-left+1) * height);
    }
    return max;
  };

  return fence(0, arr.length-1);
};

var n = 0;
require('readline').createInterface({input: process.stdin, output: process.stdout, terminal: false})
  .on('line', function (cmd) {
    if (n > 0 && n % 2 == 0) {
      var arr = cmd.split(' ').map(function(n) { return parseInt(n); });
      console.log(solv(arr));
    }
    n++;
  });
