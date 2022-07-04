# Given a string, find length of longest substring with no
# repeating characters

from cmath import exp
from struct import calcsize
from turtle import st


def no_repeat_substring(input: str):
    l = len(input)
    if l <= 1: return l
    seen = {}
    left = 0
    longest = 0
    calculations = 0
    for right in range(l):
        calculations += 1
        currentChar = input[right]
        previousIndex = seen.get(currentChar)
        if previousIndex is not None and previousIndex >= left:
            left = previousIndex + 1
        
        seen[currentChar] = right
        longest = max(longest, right - left + 1)

    # print("Calculations:", calculations, l)
    return longest
    
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
