arrs = [%w(2 2 3 3), %w(3 1 3 4 1), %w(1 1 1 1 1 1 1 2)].map { |arr| arr.map &:to_i}

f = -> ls, n=0 {
  return 0 if ls.one?
  fst, snd, *rest = ls

  n += fst + snd
  n += f.call rest.unshift(fst + snd).sort unless rest.empty?
  n
}

acc = 0
f2 = -> ls, n=0 {
  return 0 if ls.one?
  fst, snd, *rest = ls

  if snd < n
    acc += (fst + snd)
    f2.call rest << n, n + acc
  else
    acc += (fst + n)
    f2.call rest << snd, (fst + acc)
  end
}

f2.call arrs[0].sort
p acc

arrs.each do |arr|
  p arr
  p f.call arr.sort
end
