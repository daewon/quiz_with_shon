# coding: utf-8
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
  sv = -> m do
    m.inject do |acc, row|
      add = row.length < acc.length  ? 1 : -1
      row.each_with_index.map { |n, idx|
        prev_indirect = idx + add > -1 ? acc[idx + add] : 0 # 루비에서 array에 -1 인덱슬 접근시 뒤에 원소가 나온다
        n + [prev_indirect || 0, acc[idx] || 0].max
      }
    end
  end

  sv.call(matrix).first
end

# process input
for _ in 0...gets.to_i
  width = gets.to_i
  depth = width * 2 - 1
  matrix = []

  (0...depth).each do |d|
    line = gets.split.map &:to_i
    matrix[d] = line
  end

  #puts solv(width-1, depth-1, matrix)
  puts solv2(width-1, depth-1, matrix)
end
