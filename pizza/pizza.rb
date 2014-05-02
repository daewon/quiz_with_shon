require 'set'

data = [[1, 2, 3], [4, 5], [0, 2, 4], [0, 1, 5]]

seen = Set.new
solv = -> fn, nn {
  if data[fn].nil?
    p seen
    return
  end

  for i in (nn...data[fn].length)
    n = data[fn][i]
    if seen.include? n
      solv.call fn + 1, i
      return
    else
      seen << n
      solv.call fn + 1, i
      seen.delete n
    end
  end
}

solv.call 0, 0
