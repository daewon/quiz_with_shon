import os, sys

weights = {"A": 1, "C": 2, "G": 3, "T": 4}
keys = ["A", "C", "G", "T"]
def build(S):
    sz = len(S)
    R = {"A": [0] * sz, "C": [0] * sz, "G": [0] * sz, "T": [0] * sz}
    ch = S[0]
    R[ch][0] = 1
    # O(len(keys) * len(S))
    for i in range(1, sz):
        ch = S[i]
        for key in keys:
            if ch == key: R[key][i] = R[key][i-1] + 1
            else: R[key][i] = R[key][i-1]
    return R

def solution(S, P, Q):
    ranges = [(P[idx], Q[idx]) for idx in range(len(P))]
    R = build(S)
    # for key in keys:
 #        print R[key]
    ret = []
    for (i, j) in ranges:
        if i == j: 
            ret.append(weights[S[i]])
            continue
        current = weights["T"]
        for key in keys:
            if i-1 >= 0: left = R[key][i-1]
            else: left = 0
            right = R[key][j]
            if left < right: 
                current = weights[key]
                break
        ret.append(current)
    return ret

# S = "CAGCCTA"
S = "CA"
P = [0, 0, 1]
Q = [0, 1, 1]   
print solution('ACACAC', [1, 3, 4], [2, 5, 5])
# print solution(S, P, Q)
    