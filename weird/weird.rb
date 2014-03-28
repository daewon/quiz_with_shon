def divisors n
  i, acc = 1, []
  while i * i <= n
    if n % i == 0
      acc << i
      acc << n / i if n / i != n
    end
    i += 1
  end
  acc.sort.reverse
end

sub_sum = -> n, divs, i, memo do
  memo[n] = [] if memo[n].nil?

  return true if n == 0
  return false if i == -1

  return memo[n][i] unless memo[n][i].nil?
  memo[n][i] = sub_sum.call(n, divs, i-1, memo) || sub_sum.call(n - divs[i], divs, i-1, memo)
end

# WEIRD NUMBER is
# Sum of its proper divisors (i.e. less than N ) is greater than the number.
# No subset of its divisors sum to N.
is_weird = -> n do
  divs = divisors(n)
  return false if divs.inject(:+) <= n
  not sub_sum.call n, divs, divs.length-1, []
end

(0...gets.to_i).each do |_|
  if is_weird.call gets.to_i
    puts 'weird'
  else
    puts 'not weird'
  end
end
