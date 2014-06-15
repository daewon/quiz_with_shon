arr = %q{1 1 6 1 9 1 3 2 5 2 8 2 4 3 7 3 10 3 2 4 6 4 8 4 3 5 5 5 7 5}.split(" ").map(&:to_i).each_slice(2).to_a  
map = arr.each_with_object({}) do |r_c, hash| 
    r, c = r_c
    hash[[r, c]] = [r, c+1];
    hash[[r, c+1]] = [r, c];
end
sorted_keys = map.keys.sort{|a, b| a[0] <=> b[0]}

define_method :solv do |col, row=0|
  r, c = sorted_keys.detect { |r, c| r > row && c == col }        
  return col unless c || r
  r1, c1 = map[[r, c]]
  solv c1, r1
end

p solv(1)
p solv(3)
p solv(6)