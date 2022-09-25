"""
https://leetcode.com/problems/contains-duplicate/submissions/
"""


class Solution:
    def containsDuplicate(self, nums):
        if len(nums) == len(set(nums)):
            return False
        return True


class Solution:
    def containsDuplicate(self, nums):
        hashset = set()
        for n in nums:
            if n in hashset:
                return True
            hashset.add(n)
        return False
