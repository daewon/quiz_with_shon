# Given a number N, write a program that returns all possible combinations of numbers that add up to N, as lists. (Exclude the N+0=N) 
# For example, if N=4 return {{1,1,1,1},{1,1,2},{2,2},{1,3}}

# ex) input == 4
# [[1, 1, 1, 1], [1, 1, 2], [1, 3], [2, 2]]
def comb input
  acc = []
  subsets = -> prev = [] {
    ((prev.last || 1)...input).each do |n|
      set = prev.dup << n
      sum = (set.reduce :+)

      if sum == input
        acc << set # print
      elsif sum < input
        subsets.call set
      else
        return
      end
    end
    acc
  }

  subsets.call
end

p comb 4
