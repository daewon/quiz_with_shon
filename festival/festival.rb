def solv(array, n)
  avg = 10000000
  find = -> si {
    d = n
    sum = array[si..si+n-1].inject(:+)
    for i in si+n..array.length-1
      avg =  [avg, sum / d.to_f].min
      sum += array[i]
      d += 1
    end
    avg = [avg, sum / d.to_f].min
  }

  for i in 0..array.length-n
    avg = [avg, find.(i)].min
  end
  avg
end

gets.to_i.times do 
  _, n = gets.split(' ').map &:to_i
  args = gets.split(' ').map &:to_i

  min = solv args, n
  printf("%0.11f\n", min)
  # exit 
end

