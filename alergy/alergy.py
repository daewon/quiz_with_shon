import os, sys

MIN, N, M = 0, 0, 0

def solve(ps, prepared, n):
    global MIN, N, M
    if n == N:
        if len(prepared) < MIN:
            MIN = len(prepared)
        return
    if MIN <= len(prepared):
        return
    #print prepared

    for food in ps[n]:
        if food in prepared:
            solve(ps, prepared, n+1)
        else:
            prepared.add(food)
            solve(ps, prepared, n+1)
            prepared.remove(food)


T = int(raw_input())
for t in xrange(T):
    persions = {}
    n_m = [int(x) for x in raw_input().split(" ")]
    N, M = n_m[0], n_m[1]
    ps = raw_input().split(" ")
    for p in ps:
        persions[p] = set()
    for m in xrange(M):
        fs = raw_input().split(" ")
        f = int(fs[0])
        for p in fs[1:]:
            if p in persions: persions[p].add(m)
    #print persions
    ps = []
    names = []
    for (k, v) in persions.iteritems():
        ps.append(v)
        names.append(k)
    ps = sorted(ps, key=lambda x: len(x))
    #print ps, names
    MIN = M
    solve(ps, set(), 0)
    print MIN
