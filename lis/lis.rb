def lis arr
  memo = {}
  sv = -> i do
    return memo[i] if memo[i]
    m = 1
    for j in ((0...i).reject { |x| arr[x] > arr[i] }).reverse
      m = [sv.call(j) + 1, m].max
    end
    memo[i] = m
  end

  # [1, 3, 2, 1]
  (0...arr.length).to_a.reverse.map { |i| sv.(i) }.max
end

for _ in 0...gets.to_i
  gets
  puts lis gets.split.map(&:to_i)
end
