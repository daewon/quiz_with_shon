# coding: utf-8
"""
2
5 2 0
0 1 1 1 0
1 0 0 0 1
1 0 0 0 0
1 0 0 0 0
0 1 0 0 0
3
0 2 4
"""
def solv matrix, _start_point, _day, dest_point
  cache = Array.new(101)
  for i in 0..cache.length
    cache[i] = Array.new(51)
  end

  search = -> start_point, day do
    if cache[start_point][day]
      return cache[start_point][day]
    end

    if day == 0
      return dest_point == start_point ? 1.0 : 0
    end

    sum = 0
    for point in matrix[start_point]
      s = (search.(point, day-1) )
      sum += s / matrix[point].length
    end

    cache[start_point][day] = sum
    sum
  end

  search.(_start_point, _day)
end

gets.to_i.times do
  # parse input
  n, day, dest_point = gets.split(" ").map &:to_i
  m = []
  # parse matrix
  n.times do
    nums = gets.split(" ").map &:to_i
    arr = []
    nums.each_with_index do |n, i|
      arr << i if n == 1
    end
    m << arr
  end

  # dummy
  gets
  # parse q
  for point in gets.split(" ").map &:to_i
    n = solv(m, point, day, dest_point)
    printf("%0.8f ", (n))
  end
  puts ""
end
