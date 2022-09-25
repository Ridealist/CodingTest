"""
https://leetcode.com/problems/climbing-stairs/submissions/
"""


class Solution:
    def climbStairs(self, n: int) -> int:
        answer = {1: 1, 2: 2}
        for i in range(n):
            if i + 1 in answer:
                continue
            else:
                answer[i + 1] = answer[i] + answer[i - 1]
        return answer[n]


class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [0] * 100
        dp[1], dp[2] = 1, 2
        for i in range(3, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]

        return dp[n]
