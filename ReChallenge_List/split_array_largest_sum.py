"""
https://leetcode.com/problems/split-array-largest-sum/
"""

# class Solution:
#     def splitArray(self, nums: List[int], m: int) -> int:
#         answer = sum(nums)
#         for i in range(1, len(nums)-1):
#             temp = max(sum(nums[:i]), sum(nums[i:]))
#             if temp < answer:
#                 answer = temp
#         return answer


import itertools


class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:

        it = itertools.combinations(range(1, len(nums)), m - 1)
        answer = sum(nums)
        for idx in it:
            for i in idx:
                sum(nums[:i])

        for i in range(1, len(nums) - (m - 2)):
            for j in range(i + 1, len(nums)):
                temp = max(sum(nums[:i]), sum(nums[i:j]), sum(nums[j:]))
            if temp < answer:
                answer = temp
        return answer
