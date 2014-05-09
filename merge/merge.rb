def merge a, b
  return b if a.empty?
  return a if b.empty?

  a_head, *a_tail = a
  b_head, *b_tail = b

  if a_head < b_head
    [a_head] + merge(a_tail, b)
  else
    [b_head] + merge(a, b_tail)
  end
end

def merge_sort arr
  return arr if arr.one?

  n = arr.length / 2
  a, b = [arr[0...n], arr[n..-1]]
  merge merge_sort(a), merge_sort(b)
end

for i in 0..1000009
  arr = [-100, 4, 1, 2, 3, 4, 1, 1, 3, 1, 2]
  merge_sort arr
end
