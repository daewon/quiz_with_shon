# -*- coding: utf-8 -*-
"""
You have to write a function checkRegex() which takes two strings as input, one string represents a regex expression and other is an input string to match with the regex expression passed as the other parameter. Return true if it matches, else false.

Regex may contain characters ‘a-z’, ‘.’ and ‘*’ where ‘.’ matches any character and ‘*’ means 0 or more occurrences of the previous character preceding it.

Examples:

1) a*b matches b,ab,aab

2) a.b matches aab, abb, acb,…, azb

3) .* matches all the valid strings formed by using the lowercase letters
"""

def checkRegex(pattern, text):
    print pattern, text
    if len(pattern) == 0 and len(text) == 0: return True
    elif len(pattern) == 0: return False
    if len(pattern) == 1: 
        p1, p2 = pattern[0], ''
    else:
        p1, p2 = pattern[0], pattern[1]
        
    if text[0] == p1:
        if p2 == '*':
            j = 0
            while text[j] == p1: j += 1
            return checkRegex(pattern[2:], text[j:])
        else:
            return checkRegex(pattern[1:], text[1:])
    else:
        if p1 == '.':
            if p2 == '*': return True
            else: return checkRegex(pattern[1:], text[1:])
        else:
            if p2 == '*': return checkRegex(pattern[2:], text)
            else: return False


print checkRegex("a*b", "b")
print checkRegex("a*b", "ab")
print checkRegex("a*b", "aabb")

                