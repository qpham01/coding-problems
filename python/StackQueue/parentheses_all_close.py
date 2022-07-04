# Given a string with only parentheses, determine if all
# parentheses close
from collections import deque

def parentheses_all_close(input:str):
    matching = {'(':')', '{':'}', '[':']'}
    stack = deque()
    for c in input:
        if c in matching: stack.append(c)
        else:
            if len(stack) == 0: return False
            m = stack.pop()
            if c != matching[m]: return False
            
    return len(stack) == 0

def test(input: str, expected: bool):
    result = parentheses_all_close(input)
    print(result)
    assert result == expected
    
test("()", True)
test("(", False)
test(")", False)
test("())", False)
test("()(", False)
test("(()", False)
test("(()(", False)
test("()(()())", True)
test("{[]()}", True)
test("(){[]()}", True)
test("(){[](]}", False)
test("(){[](()[{}])}{[[[]]()]{}}", True)
test("(){[](()[{}]{[[[]]()]{}})}", True)
test("(){[](()[{}]{[[[]]()]{})}}", False)
