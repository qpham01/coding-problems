#Given an array of integers, return the indices of the two numbers that add up to a given target
#Use hash table to find other part of the sum to target quickly.

def twoSums(inputs: list, target: int):
    indices = {}
    n = len(inputs)
    for i in range(n):
        input = inputs[i]
        other = target - input
        if other in indices and indices[other] != i:
            return [indices[other], i]
        else:
            indices[input] = i
    return None

answer = twoSums([3,2,4], 6)
print(answer)
assert answer == [1, 2]

answer = twoSums([3,2,3,4], 6)
print(answer)
assert answer == [0, 2]

answer = twoSums([1, 3, 7, 9, 2], 11)
print(answer)
assert answer == [3, 4]

answer = twoSums([1, 3, 7, 9, 2], 25)
print(answer)
assert answer == None

answer = twoSums([], 5)
print(answer)
assert answer == None

answer = twoSums([5], 5)
print(answer)
assert answer == None

answer = twoSums([1, 5], 6)
print(answer)
assert answer == [0, 1]
