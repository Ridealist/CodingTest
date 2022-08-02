"""
https://leetcode.com/problems/contains-duplicate/submissions/
"""


class Solution:
    def containsDuplicate(self, nums):
        memory = None
        for i in nums:
            if memory == i:
                return False
            memory = i
        return True
