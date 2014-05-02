def is_prime n
  return true if n <= 2
  (2..(n / 2)).each do |curr|
    return false if n % curr == 0
  end
  true
end

def prime_factor n
  primes, curr, div = [], n, 2

  while curr > 2
    if curr % div == 0
      primes << div
      curr = curr / div
    else
      div += 1
    end
  end
  primes
end

n = 100
p n
a = prime_factor n
p a, a.inject(:*)
