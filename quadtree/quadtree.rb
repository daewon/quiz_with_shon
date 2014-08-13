class Tree
  attr_accessor :ch, :lt, :rt, :lb, :rb, :parent

  def initialize ch, parent=nil
    @state, @ch, @parent = 0, ch, parent
  end

  def is_full?
    @state == 4
  end

  def reverse!
    @lt, @rt, @lb, @rb = @lb, @rb, @lt, @rt
    [@lt, @rt, @lb, @rb].select { |n| n.is_a? Tree }.map &:reverse!
    self
  end

  def add node
    raise if is_full?
    case @state
    when 0
      @lt = node
    when 1
      @rt = node
    when 2
      @lb = node
    when 3
      @rb = node
    end
    @state += 1
  end

  def to_s
    @ch + [@lt, @rt, @lb, @rb].map(&:to_s).join('')
  end
end

def solv line
  parse = -> tree, input do
    return tree if input.empty?

    if tree.is_full?
      parse.(tree.parent, input)
    else
      ch = input.delete_at 0
      if ch == 'x'
        new_tree = Tree.new ch, tree
        tree.add new_tree
        parse.(new_tree, input)
      else
        tree.add ch
        parse.(tree, input)
      end
    end
  end

  head, *tail = line
  tree = Tree.new head
  return parse.(tree, tail).reverse!
end

gets.to_i.times do
  puts solv gets.strip.split('')
end
