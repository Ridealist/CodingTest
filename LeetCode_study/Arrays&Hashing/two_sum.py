"""
https://leetcode.com/problems/two-sum/submissions/
"""


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for idx, n in enumerate(nums):
            if (target - n) in nums[idx + 1 :]:
                # print(n, target-n)
                if target - n == n:
                    return [nums.index(n), nums.index(n, nums.index(n) + 1)]
                return [nums.index(n), nums.index(target - n)]


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for idxn, n in enumerate(nums):
            for idxs, s in enumerate(nums[idxn + 1 :]):
                if n + s == target:
                    return [idxn, idxn + 1 + idxs]


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevMap = {}  # val -> index

        for i, n in enumerate(nums):
            diff = target - n
            if diff in prevMap:
                return [prevMap[diff], i]
            prevMap[n] = i
