def bracket arr
  arr = arr.split ''
  pair = {"(" => ")", "[" => "]"}
  cache = {}

  solv = -> i, j do
    return 0 if (j-i) < 1
    return cache["#{i}_#{j}"] if cache["#{i}_#{j}"]

    start_ch, last_ch = arr[i], arr[j]
    a, b, c = 0, 0, 0

    if pair[start_ch] and pair[start_ch] == last_ch # match () || []
      a = 2 + solv.(i+1, j-1)
    end

    b = solv.(i+1, j)

    match = []
    idx = i
    while idx <= j
      ch = arr[idx]
      if start_ch == "(" and ch == ")"
        match << idx
      elsif start_ch == "[" and ch == "]"
        match << idx
      end
      idx += 1
    end

    c = 0
    for idx in match
      c = [c, 2 + solv.(i+1, idx-1) + solv.(idx+1, j)].max
    end

    m = [a, b, c].max
    cache["#{i}_#{j}"] = m
    m
  end

  solv.(0, arr.length-1)
end

loop do
  line = gets.strip
  break if line == "end"
  puts bracket line
end
