#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
double  solveForX(string s) {   }

input will be linear equation in x with +1 or -1 coefficient.

output will be value of x.

s can be as follows

i/p   x + 9 – 2 -4 + x = – x + 5 – 1 + 3 – x   o/p  1.00

i/p    x + 9 -1 = 0  o/p -8.00

i/p    x + 4 = – 3 – x  o/p  -3.500

it has second part

if the i/p string can have ‘(‘ or  ‘)’

x + 9 – 2 -(4 + x) = – (x + 5 – 1 + 3) – x

x + 9 + (3 + – x – ( -x + (3 – (9 – x) +x = 9 -(5 +x )
"""

"""
 a + b x c - 4 = abcx+4-
 a + ((b + c) - d) = abc+d-+
"""
operators = {'+': 1, '-': 1, 'x': 2, '/': 2}


def operate(op, x, y):
    if op == '+': z = x + y
    elif op == '-': z = x - y
    elif op == 'x': z = x * y
    elif op == '/': z = x / y
    else: z = None
    return z
#s = "10 + ((4 x 2) - 4)"
def infixToPrefix(s):
    ops = []
    nums = []
    arr = s.split()
    print arr
    for (i, e) in enumerate(arr):
        print ops, nums
        if e == '(':
            ops.append((e, 0))
        elif e == ')':
            while len(ops) > 0:
                (op, top) = ops.pop()
                if op == '(': break
                y, x = nums.pop(), nums.pop()
                z = operate(op, x, y)
                if z: nums.append(z)
        elif e in operators: 
            if len(ops) == 0: ops.append((e, operators[e]))
            else:
                (op, top) = ops[-1]
                cur = operators[e]
                if cur > top: ops.append((e, cur))
                else:
                    while cur <= top and len(ops) > 0:
                        (op, top) = ops.pop()
                        y, x = nums.pop(), nums.pop()
                        z = operate(op, x, y)
                        if z: nums.append(z)
                    ops.append((e, operators[e]))
        else:
            nums.append(int(e))          

    while len(ops) > 0 and len(nums) > 1:
        (op, top) = ops.pop()
        y, x = nums.pop(), nums.pop()
        z = operate(op, x, y)
        if z: nums.append(z)
    return nums
          
def solveForX(s):
    (coefs, constants) = parse(s)
    print coefs, constants
    return constants / (-1.0 * coefs)
    
def parse(s):
    s = s.split()
    print s
    coefs = 0
    cons = 0
    op = 1
    isLeft = True
    for (i, e) in enumerate(s):
        if e == '=': 
            isLeft = False
            continue
        if e == '': continue
        if e == '+' or e == '-' or e == '\xe2\x80\x93': 
              if e == '-' or e == '\xe2\x80\x93': op = -1
              else: op = 1
              continue
        if e == 'x':
            if isLeft: coefs += op
            else: coefs += -1 * op
            continue
        if isLeft: cons += op * int(e)
        else: cons += op * -1 * int(e)
        
        
    return (coefs, cons)
    
s = "x + 9 – 2 - 4 + x = – x + 5 – 1 + 3 – x"
s = "x + 9 - 1 = 0"
s = "x + 4 = – 3 – x"
s = "10 + 4 x 2 - 4"
#s = "10 + ( ( 4 x 2 ) - 4 )"
print infixToPrefix(s)
#print solveForX(s)