def solv txt
  words = txt.gsub(/([a-z])-\$\n([a-z])/, '\1\2').split(/[-$ \n]/).reject &:empty?
  puts sprintf("%.3f", words.join.length / words.length.to_f)
end

t = gets.to_i
(0...t).each { |_n|
  l = gets.to_i
  arr = []
  (0...l).each { |n|
    arr << gets
  }
  solv(arr.join)
}
