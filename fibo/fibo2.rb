# 0 1 1 2 3 5 8 13 ... N

def fibo(n)
  # throw if n is negative
  i = 0
  acc = []
  prev, current = 0, 1
  while i < n
    acc << current
    prev, current = current, (prev + current)

    i += 1
  end
  acc
end

p fibo(1000)
