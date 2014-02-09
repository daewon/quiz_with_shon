#! /usr/bin/python 

import os, sys 
N, M = 4, 6 
#N, M = 6, 10 
G = {} 
#pairs = [0, 1, 1, 2, 2, 3, 3, 0, 0, 2, 1, 3] 
#pairs = [0,1, 0, 2, 1, 2, 1, 3, 1, 4, 2, 3, 2, 4, 3, 4, 3, 5, 4, 5] 
pairs = [0,1,0,2,1,0,2,0,2,3,3,2] 
seen = {} 

def build_graph(): 
   for i in xrange(0, len(pairs)-1, 2): 
       x, y = pairs[i], pairs[i+1] 
       if x not in G: G[x] = {} 
       if y not in G: G[y] = {} 
       G[x][y] = 1 
       G[y][x] = 1 
   for i in xrange(0,N): 
       seen[i] = False 
        
def solve(u): 
   print u, seen 
   ret = 0 
   if u == -1: 
       print "bottom" 
       return 1 
   if seen[u]: return 0 

   seen[u] = True 
   for (v, w) in G[u].iteritems(): 
       if seen[v]: continue 
        
       seen[v] = True 
       candidate = -1 
       #for k in xrange(u+1, N): 
       for k in xrange(u+1, N): 
           if seen[k] == False: 
               candidate = k 
               break 
       print "use: %d, %d" % (u, v) 
       ret += solve(candidate) 
       print "pop: %d, %d" % (u, v) 
       seen[v] = False 
   seen[u] = False 
   return ret 
    
build_graph() 
print G 
print solve(0)
