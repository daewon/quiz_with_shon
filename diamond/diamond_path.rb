# dp
def solv width, depth, matrix, memo = []
  sv = -> w, d do
    return 0 if w == -1 || w > width || d == -1

    memo[d] = [] if memo[d].nil?
    return memo[d][w] unless memo[d][w].nil?

    add = d > width ? 1 : -1
    memo[d][w] = [sv.call(w, d-1), sv.call(w + add, d-1)].max + (matrix[d][w] || 0)
  end
  sv.call 0, depth
end

# greedy
def solv2 width, depth, matrix
  a, b = matrix[0..width].reverse, matrix[(width+1)..depth]
  sv = -> m do
    m.inject do |acc, row|
      row.each_with_index.map do |n, idx|
        [n + acc[idx], n + acc[idx+1]].max
      end
    end
  end

  sv.call(a).first + sv.call(b).first
end

# process input
n = gets.to_i
for _ in 0...n
  width = gets.to_i
  depth = width * 2 - 1
  matrix = []
  for d in 0...depth
    line = gets.split.map &:to_i
    matrix[d] = line
  end

  puts solv(width-1, depth-1, matrix)
  puts solv2(width-1, depth-1, matrix)
end
