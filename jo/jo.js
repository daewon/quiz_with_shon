var solv = function(n, k) {
  var nodes = [];
  for (var i=1; i<=n; i++) {
    nodes.push({value: i});
  }

  for (var i=0; i < nodes.length; i++) {
    nodes[i].prev = nodes[i-1];
    nodes[i].next = nodes[i+1];
  }

  nodes[0].prev = nodes[nodes.length-1];
  nodes[nodes.length-1].next = nodes[0];

  var i = 1;
  var node = nodes[0];
  while (n > 2) {
    if (i % k == 1) {
      node.next.prev = node.prev;
      node.prev.next = node.next;
      n--;
    }
    node = node.next;
    i++;
  }

  console.log(node.value, node.next.value);
};

var n = 0;
require('readline').createInterface({input: process.stdin, output: process.stdout, terminal: false})
  .on('line', function (cmd) {
    if (n > 0) {
      var arr = cmd.split(' ').map(function(n) { return parseInt(n); });
      solv(arr[0], arr[1]);
    }
    n++;
  });
