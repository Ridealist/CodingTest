"""
https://leetcode.com/problems/min-cost-climbing-stairs/
"""


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:

        cost.append(0)
        for i in range(len(cost) - 3, -1, -1):
            cost[i] += min(cost[i + 1] + cost[i + 2])

        return min(cost[0], cost[1])


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cost.append(0)
        for i in range(2, len(cost)):
            if cost[i - 1] > cost[i - 2]:
                cost[i] += cost[i - 2]
            elif cost[i - 1] <= cost[i - 2]:
                cost[i] += cost[i - 1]
        return cost[-1]


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:

        cost.append(0)
        for i in range(2, len(cost)):
            cost[i] += min(cost[i - 1], cost[i - 2])
        return min(cost[-1], cost[-2])
