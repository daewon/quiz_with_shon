def load():
  G = {}
  l = raw_input().strip().split()
  N, M = int(l[0]), int(l[1])
  for n2 in range(M):
    points = raw_input().strip().split()
    U, V, W = int(points[0]), int(points[1]), int(points[2])
    if U not in G: G[U] = {}
    if V not in G[U]: G[U][V] = set()
    G[U][V].add(W)
    if V not in G: G[V] = {}
    if U not in G[V]: G[V][U] = set()
    G[V][U].add(W)

  return G

# s: current point in graph
# g: graph
# seen: seen node
memo = {}
def solv(c, g, seen):
  if c in memo: return
  if (c == len(g)-1):
    memo[c] = set([(1000, 0)])
    return

  tmp = set()
  for v in g[c]: # trakverse friends
    if (v in seen): continue
    seen.add(v) # seen current node
    solv(v, g, seen)
    seen.remove(v)

    for (x, y) in memo[v]:
      for w in g[c][v]:
        tmp.add((min(x, w), max(y, w)))

  memo[c] = tmp

for n in range(int(raw_input())):
  g = load()
  print(g)
  solv(0, g, set([0]))
  print(memo)
  print(min([(y - x) for (x, y) in memo[0]]))
  memo = {}
  print('\n')
