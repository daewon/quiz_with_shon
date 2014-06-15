def solv n, prev = []
  return if prev.inject(0, :+) > n
  if (prev.inject :+) == n
    return p prev
  end

  (1..n).each do |i|
    dp = prev.dup << i
    solv(n, dp)
  end
end

solv 3
