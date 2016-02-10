

# B[i] = subarray with min average from somewhere from k <= i and ending at i.
# B[i] = min((B[i-1] + A[i] / (C[i-1] + 1)), A[i])
def solve(A_param):
    A = [float(x) for x in A_param]
    B = [0.0 for i in range(len(A))]
    C = [0.0 for i in range(len(A))]
    ret = (A[0] + A[1]) / 2
    B[0] = A[0]
    B[1] = ret
    C[0] = 0
    C[1] = 0
    # print A
    for i in range(2, len(A)):
        old_len = i-1 - C[i-1] + 1
        using = (B[i-1] * old_len + A[i]) / (old_len + 1)
        not_using = (A[i-1] + A[i]) / 2
        # print i, using, not_using
        if using < not_using:
            B[i] = using
            C[i] = C[i-1]
        else:    
            B[i] = not_using
            C[i] = i-1
            
    #     print B
    #     print C
    # print "*" * 10
    # print A
    # print B
    # print C
    ret = 0
    min_value = 1000000
    for i in range(1, len(A)):
        if B[i] < min_value: 
            min_value = B[i]
            ret = C[i]
    return ret
    
            
def solution(A):
    # write your code in Python 2.7
    return solve(A)

A = [-3, -5, -8, -4, -10]    
print solution(A)    
