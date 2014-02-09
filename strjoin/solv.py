import heapq
inputs = [[2, 2, 4], [3, 1, 3, 4, 1], [1, 1, 1, 1, 1, 1, 1, 2]]

def solv(ls):
  acc, hq = 0, sorted(ls)

  for n in xrange(len(hq)-1):
    a, b = heapq.heappop(hq), heapq.heappop(hq)
    sum = a + b
    heapq.heappush(hq, sum)
    acc += sum

  return acc

for input in inputs:
  print(input, solv(input))
