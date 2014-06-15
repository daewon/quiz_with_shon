#arr = %q{-1000 -1000 -3 -1000 -1000}.split(" ").map &:to_i
#arr = %q{100 -1000 -1000 100 -1000 -1000}.split(" ") .map &:to_i
#arr = %q{7 -5 8 5 1 -4 -8 6 7 9}.split(" ") .map &:to_i

def solv(arr)
  memo = {}
  number = -> i, j do
    return arr[i] if j-i == 0
    return 0 if j-i < 0
    memo[i] = {} unless memo[i]
    return memo[i][j] if memo[i][j]

    a = arr[i] - number.call(i+1, j)
    b = arr[j] - number.call(i, j-1)
    c, d = 0, 0

    if (j-i > 1)
      c = 0 - number.call(i+2, j)
      d = 0 - number.call(i, j-2)
    end
    
    memo[i][j] = [a, b, c, d].max    
    
    end
  number.call(0, arr.length - 1)
end

(0...gets.to_i).each do |_|
  gets
  arr = gets.split(" ").map &:to_i  
  puts solv(arr)  
end
