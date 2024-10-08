"""
70. Climbing Stairs
Solved
Easy
Topics
Companies
Hint
You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

 

Example 1:

Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps
Example 2:

Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step"""
class Solution(object):
    memo={}
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        ######### Solution 1: Bottom-up: More intuitive
        # sol = [0,1,2]
        # for i in range(3,n+1):
        #     temp = sol[i-1] + sol[i-2]
        #     sol.append(temp)
        # return sol[n]

        ##### Solution 2: F(n) = F(n-1) + F(n-2) ######### top down
        if n in self.memo:
            return self.memo[n]
        if n == 1:
            return 1
        elif n == 2:
            return 2

        # Store the result in the memo dictionary
        self.memo[n] = self.climbStairs(n - 1) + self.climbStairs(n - 2)
        return self.memo[n]

