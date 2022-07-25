import math

def solution(N):
    # write your code in Python 3.6
    if N < 10: return N
    digits = []
    count = math.ceil(math.log10(N + 1))
    for i in range(count):
        d = N % 10
        digits.append(d)
        N = N // 10
    digits.sort()
    maxN = 0
    for i in range(len(digits)):
        maxN += digits[i] * (10**i)
    if maxN > 100000000:
         return -1
    return maxN

assert solution(0) == 0
assert solution(1) == 1
assert solution(12) == 21
assert solution(123) == 321
assert solution(355) == 553
assert solution(99999999) == 99999999
assert solution(100000000) == 100000000
assert solution(100000001) == -1
assert solution(23456789) == 98765432
assert solution(123456789) == -1
