gets.to_i.times do
  matrix = []
  words = []
  5.times do
    matrix << gets.strip.split('')
  end
  gets.to_i.times do
    words << gets.strip
  end
  puts matrix.map(&:join).join("\n")
end


