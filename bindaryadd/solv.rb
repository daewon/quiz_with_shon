# You have two numbers decomposed in binary representation, write a function that sums them and returns the result. 
# Input: 100011, 100100 
# Output: 1000111

arr = [1, 0, 0, 0, 1, 1].zip([1, 0, 0, 1, 0, 0])
p "input: #{arr}"

res = arr.reverse.inject({carry: 0, result: []}) {|acc, (a, b)|
  sum = a + b + acc[:carry]
  acc[:result].push((sum == 1) ? 1 : 0)
  acc[:carry] = (sum > 1) ? 1 : 0
  acc
}

res[:result] << 1 if res[:carry] > 0

p "expected: #{[1, 0, 0, 0, 1, 1, 1]}"
p "result: #{res[:result].reverse}"
