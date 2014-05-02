def lis arr
  memo = {}
  sv = -> i do
    return 1 if i == 0
    return 0 if i < 0
    return memo[i] if memo[i]
    m = 1
    (0...i).each do |j|
      next if arr[j] > arr[i]
      a = sv.call(j) + 1
      m = [a, m].max
    end
    memo[i] = m
  end

  p sv.call 1
  #(0...arr.length).map { |i| sv.call i }.max
end

lis [3, 4, 1, 2]
# for _ in 0...gets.to_i
#   gets
#   p lis(gets.split.map(&:to_i))
# end
