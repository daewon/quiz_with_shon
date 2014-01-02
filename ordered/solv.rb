# -*- coding: utf-8 -*-
# Epic Systems Interview Question
# Given n. Generate all numbers with number of digits equal to n, such that the digit to the right is greater than the left digit (ai+1 > ai). E.g. if n=3 (123,124,125,……129,234,…..789)

limit = 3
ordered = -> prev {
  if prev.length == limit
    p prev
    return
  end

  last = prev[-1].to_i
  (1..9).each { |n|
    next if n <= last
    ordered.call("#{prev}#{n}")
  }
}

ordered.call("")
