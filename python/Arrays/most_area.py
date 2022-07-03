# Given array of positive integers where each represent heigh of vertical line on a chart, find two
# lines which together with x axis forms greatest area with the shorter of the two lines.  Return 
# the greatest area.

def mostArea(inputs: list):
    l = len(inputs)
    if l == 0 or l == 1: return 0
    max_area = 0
    p1 = 0
    p2 = l - 1
    calculations = 0
    while (p1 < p2):
        calculations += 1
        h1 = inputs[p1]
        h2 = inputs[p2]
        min_h = min(h1, h2)
        area = min_h * (p2 - p1)
        max_area = max(max_area, area)
        # print(max_area, p1, p2)            
        if h1 <= h2:
            p1 += 1
        else:
            p2 -= 1
    print("Calculations", calculations)
    return max_area


answer = mostArea([4, 8, 1, 2, 3, 9])
print(answer)
assert answer == 32

answer = mostArea([])
print(answer)
assert answer == 0

answer = mostArea([5])
print(answer)
assert answer == 0

answer = mostArea([7,1,2,3,9])
print(answer)
assert answer == 28

answer = mostArea([1,7,2,8,1,6])
print(answer)
assert answer == 24

answer = mostArea([6, 9, 3, 4, 5, 8])
print(answer)
assert answer == 32