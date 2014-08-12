def solv m
  len = m.length-1
  memo = Hash.new {|h, k| h[k] = []}
  m[len].each_with_index { |n, idx| memo[len][idx] = n } # set bottom

  i = len-1
  while i >= 0
    m[i].each_with_index do |n, c|
      a = memo[i+1][c] + n
      b = memo[i+1][c+1] + n
      memo[i][c] = [a, b].max
    end
    i -= 1
  end

  return memo[0][0]
end

gets.to_i.times do
  m = []
  gets.to_i.times do
    m << gets.split(" ").map(&:to_i)
  end
  p solv(m)
end
