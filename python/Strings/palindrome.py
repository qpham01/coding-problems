from doctest import FAIL_FAST
import re

def strip_non_alphanumeric(input:str) -> str:
    temp = re.sub("[^\w]", "", input)
    temp = temp.lower()
    return temp

assert strip_non_alphanumeric("Race 1 :e caR") == "race1ecar"
assert strip_non_alphanumeric("A man, a plan, a canal: Panama!") == "amanaplanacanalpanama"
    
def is_palindrome(input:str) -> bool:
    temp = strip_non_alphanumeric(input)
    size = len(temp)
    if size == 0 or size == 1: return True
    p1 = 0
    p2 = size - 1
    while p1 < p2:
        if temp[p1] != temp[p2]: return False
        p1 += 1
        p2 -= 1
        
    return True

assert is_palindrome("") is True
assert is_palindrome("a") is True
assert is_palindrome("aba") is True
assert is_palindrome("abb") is False
assert is_palindrome("race car") is True
assert is_palindrome("race a car") is False
assert is_palindrome("Race 1 :e caR") is True
assert is_palindrome("racie car") is False
assert is_palindrome("A man, a plan, a canal: Panama!") is True
assert is_palindrome("") is True
assert is_palindrome("5") is True
assert is_palindrome("5a5") is True
assert is_palindrome("123") is False
assert is_palindrome("3b b3") is True
assert is_palindrome("7c1c7") is True

def almost_palindrome_check(input:str, p1:int, p2:int, remove_count:int, max_remove:int) -> bool:
    while p1 < p2:
        if input[p1] != input[p2]:
            remove_count += 1
            if remove_count > max_remove: return False
            if almost_palindrome_check(input, p1 + 1, p2, remove_count, max_remove): return True
            if almost_palindrome_check(input, p1, p2 - 1, remove_count, max_remove): return True
        p1 += 1
        p2 -= 1        
    return True

def almost_palindrome(input:str, max_remove:int) -> bool:
    temp = strip_non_alphanumeric(input)
    size = len(temp)
    if size == 0 or size == 1: return True
    p1 = 0
    p2 = size - 1
    remove_count = 0
    return almost_palindrome_check(temp, p1, p2, remove_count, max_remove)

assert almost_palindrome("abcdefdba", 1) is False
assert almost_palindrome("abccdba", 1) is True
assert almost_palindrome("raceacar", 1) is True
assert almost_palindrome("abcdfdba", 2) is True
