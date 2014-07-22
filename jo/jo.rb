class Node
  attr_accessor :value, :next_node,:prev_node
  def initialize value, next_node=nil
    @value = value
    @next_node, @prev_node = next_node, prev_node
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
    if i % k == 1 
      pr = node.prev_node
      ne = node.next_node
      node.next_node.prev_node = pr
      node.prev_node.next_node = ne
      n -= 1
    end
    node = node.next_node
    i += 1
  end

  "#{node.value} #{node.next_node.value}"
end

gets.to_i.times do
  n, k = gets.split(" ").map &:to_i
  puts solv n, k
end

