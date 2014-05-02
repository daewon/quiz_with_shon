def comb arr
  ret = []
  solv = -> i, prev = "" do
    (i...arr.length).each do |k|
      pr = prev.dup << arr[k]
      ret << pr
      solv.call(k+1, pr)
    end
  end
  solv.call 0
  ret
end
alias :subsets :comb

def perm arr
  ret, seen = [], {}
  solv = -> i, prev do
    (i...arr.length).each do |k|
      if prev.length == arr.length
        ret << prev.join
        return
      end

      next if seen[arr[k]]
      seen[arr[k]] = true
      pr = prev.dup << arr[k]
      solv.call i, pr
      seen[arr[k]] = false
    end
  end
  solv.call 0, []
  ret
end

def remove_duplicate arr
  tail = 1
  find_befor = -> i do
    for j in 0...i
      return  true if arr[i] == arr[j]
    end
    false
  end

  for i in 1...arr.length
    unless find_befor.call i
      arr[tail] = arr[i]
      tail += 1
    end
  end

  arr[0...tail]
end

arr = "xyzw".split ""
# p comb arr
# p perm arr
p remove_duplicate "aaabbbbbbccc".split ""
