# You are a professional robber planning to rob houses along a street. 
# Each house has a certain amount of money stashed, the only constraint 
# stopping you from robbing each of them is that adjacent houses have 
# security systems connected and it will automatically contact the police 
# if two adjacent houses were broken into on the same night.

# Given an integer array nums representing the amount of money of each house, 
# return the maximum amount of money you can rob tonight without alerting 
# the police.

class Solution(object):
    def rob(self, nums: list):
        count = len(nums)
        if (count == 1): return nums[0]
        prev2 = nums[0]
        prev1 = max(nums[0], nums[1])
        best = 0
        for i in range(2, count):
            best = max(nums[i] + prev2, prev1)
            prev2 = prev1
            prev1 = best
            
        return best
            
solution = Solution()
answer = solution.rob([1,2,3,1])
print(answer)
assert answer == 4

answer = solution.rob([2,7,9,3,1])
print(answer)
assert answer == 12