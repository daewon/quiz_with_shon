# merge a with b
def merge a, b
  if a.empty? and (not b.empty?)
    return b
  elsif b.empty? and (not a.empty?)
    return a
  else
    a_head, *a_tail = a
    b_head, *b_tail = b

    if a_head <= b_head
      [a_head] + merge(a_tail, b)
    else
      [b_head] + merge(a, b_tail)
    end
  end
end

# split array
def msort arr
  return arr if arr.one?
  return [] if arr.empty?

  pivot = arr.length / 2
  l = msort(arr[0..pivot-1]) || []
  r = msort(arr[pivot..-1]) || []

  merge msort(l), msort(r)
end


puts "\nres: #{msort([5, 6, 1])}"
puts (0..2).to_a.sort == msort((0..2).to_a.shuffle)
puts (0..10).to_a.sort == msort((0..10).to_a.shuffle)
