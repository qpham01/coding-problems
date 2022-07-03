# You are climbing a staircase. It takes n steps to reach the top.
# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
# https://www.youtube.com/watch?v=Y0lT9Fck7qI&t=1015s
# Solution
# - Create a decision tree at each step.
# - Identify sub-trees as subproblems.
# - Work backwards from bottom using "bottom-up dynamic programming".
# - Instead of array, use just enough variables to hold intermediate computes.
# - Show that problem is same as Fibonacci sequence.

class Solution:
    def climbStairs(self, n: int) -> int:
        one, two = 1, 1
        for i in range(n - 1):
            temp = one
            one = one + two
            two = temp
        
        return one
  
def testClimbingStairs():  
    inputs = [1, 2, 3, 4, 5]
    expected = [1, 2, 3, 5, 8]

    solution = Solution()

    for i in range(len(inputs)):
        answer = solution.climbStairs(inputs[i])
        if (answer != expected[i]):
            raise Exception;
    
    print("climbingStairs passed!") 
        
testClimbingStairs()