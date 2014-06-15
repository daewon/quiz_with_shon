def solv n
  count, used = 0, {}
  queen = -> row do
    if row == n
      count += 1
      return
    end

    for col in 0...n
      l, c, r = row-col-1000, col, row+col+1000
      next if used[l] || used[c] || used[r]

      used[l], used[c], used[r] = true, true, true
      queen.(row + 1)
      used[l], used[c], used[r] = nil, nil, nil
    end
  end

  queen.(0)
  count
end

n = gets.to_i
n.times do
  puts solv gets.to_i
end
