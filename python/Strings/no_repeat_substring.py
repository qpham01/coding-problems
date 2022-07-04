# Given a string, find length of longest substring with no
# repeating characters

from cmath import exp
from turtle import st


def no_repeat_substring(input: str):
    l = len(input)
    if l == 0: return 0
    if l == 1: return 1
    maxLen = 1
    curLen = 1
    start = 0
    end = 1
    chars = {input[start]}
    calculations = 0
    while (end < l):
        calculations += 1
        currentChar = input[end]
        if currentChar not in chars:
            curLen = end - start + 1
            maxLen = max(curLen, maxLen)
            chars.add(currentChar)
            end += 1
        else:
            if (start < l - 1):
                start += 1
                end = start + 1
                chars = {input[start]}
            
    print("Calculations:", calculations, l)
    return maxLen
    
def test(input: str, expected:int):
    a = no_repeat_substring(input)
    print(input, a)
    assert a == expected

test("", 0)
test("a", 1)
test("ccc", 1)
test("abc", 3)
test("aabcdd", 4)
test("abcdd", 4)
test("abccde", 3)
test("abccab", 3)
test("abcabcbb", 3)
test("dvdf", 3)
test("abcabcbbabcabcbbabcabcbb", 3)
