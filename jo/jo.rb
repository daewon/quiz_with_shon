class Node
  attr_accessor :value, :next_node, :prev_node
  def initialize value
    @value = value
  end
end

def solv n, k
  input = (1..n).map &:to_i
  nodes = input.map { |n| Node.new n }
  nodes.each_cons(2) { |a, b| a.next_node = b; b.prev_node = a }
  nodes.last.next_node = nodes.first
  nodes.first.prev_node = nodes.last

  i = 1
  node = nodes.first
  while n > 2
    if i % k == 1 or k == 1
      node.next_node.prev_node = node.prev_node
      node.prev_node.next_node = node.next_node
      n -= 1
    end
    node = node.next_node
    i += 1
  end

  "#{[node.value, node.next_node.value].sort.join(' ')}"
end

gets.to_i.times do
  n, k = gets.split(" ").map &:to_i
  puts solv n, k
end
