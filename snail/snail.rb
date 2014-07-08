CACHE = Array.new(100)
for i in 0..CACHE.length
  CACHE[i] = Array.new(1000)
end

def solv depth, day
  def snail m, n
    return 0 if n < 0
    return 1 if m <= 0
    return CACHE[m][n] if CACHE[m] and CACHE[m][n]

    a = 0.75 * snail(m-2, n-1)
    b = 0.25 * snail(m-1, n-1)


    CACHE[m][n] = a+b
  end

  snail depth, day
end

gets.to_i.times do
  m, n = gets.split.map(&:to_i)
  printf("%0.10f\n", solv(m, n ))
end
