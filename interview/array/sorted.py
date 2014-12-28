#1. Find two elements in sorted array which sums to a given number (code it)

def findTwoElement1(arr, k):
    ret = []
    sz = len(arr)
    for i in range(sz):
        x = arr[i]
        for j in range(i + 1, sz):
            y = arr[j]
            if x + y == k: ret.append((i, j))
    return ret

def find(arr, x):
    return findInner(arr, 0, len(arr)-1, x)
    
def findInner(arr, left, right, x):
    if left > right: return -1
    if left == right and arr[left] == x: return left
    mid = (left + right) / 2
    if arr[mid] == x: return mid
    elif x < arr[mid]: return findInner(arr, left, mid - 1, x)
    else: return findInner(arr, mid + 1, right, x)
    
    
def findTwoElement2(arr, k):
    ret = []
    sz = len(arr)
    for i in range(sz):
        idx = find(arr, k - arr[i])
        print i, idx
        if idx != -1: ret.append((i, idx))
    return ret
    
arr = sorted([1, 2, 1, 2, 3, 1, 4, 3, 2])
print arr
print findTwoElement2(arr, 7)
            