# R, C = 3, 7
# M = """#.....#
# #.....#
# ##..###""".split("\n").map {|line| line.split('')}

M = """##########
#........#
#........#
#........#
#........#
#........#
#........#
##########""".split("\n").map { |line| line.split('') }
R, C = 8, 10

show = -> { puts M.map { |line| line.join('') } }
def generate r, c
  [[[r, c+1], [r+1, c]],
   [[r, c-1], [r+1, c]],
   [[r, c+1], [r+1, c+1]],
   [[r, c-1], [r+1, c-1]],
   [[r+1, c], [r+1, c+1]],
   [[r+1, c], [r+1, c-1]],
  ].map { |line| line << [r, c] }
end

def filter poses
  poses.select { |line|
    line.all? { |(r, c)|
      r >= 0 and c >= 0 and c < C and r < R and M[r][c] != '#'
    }
  }
end

place = -> ch, pos { pos.each { |(r, c)| M[r][c] = ch } }
cnt = 0
run = -> pr, pc do
  si, sj = -1, -1
  catch :find do
    (pr...R).each { |r|
      (pc...C).each { |c|
        if M[r][c] === '.'
          si, sj = r, c
          throw :find
        end
      }
    }
  end

  cnt += 1 if si == -1 and sj == -1
  filter(generate(si, sj)).each { |pos|
    place.call '#', pos
    run.call si, si != pr ? 0 : pc
    place.call '.', pos
  }
end

run.call 0, 0
p cnt
