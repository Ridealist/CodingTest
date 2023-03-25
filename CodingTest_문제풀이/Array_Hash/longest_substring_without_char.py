# https://leetcode.com/problems/longest-substring-without-repeating-characters/description/


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        print(s)
        res = 0
        l, r = 0, 0
        sub = []
        while r < len(s):
            if s[r] not in sub:
                sub.append(s[r])
                if len(sub) > res:
                    res = len(sub)
                r += 1
            else:
                sub.pop(0)
                l += 1
        return res
