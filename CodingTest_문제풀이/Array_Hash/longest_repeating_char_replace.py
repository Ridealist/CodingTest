# https://leetcode.com/problems/longest-repeating-character-replacement/


from collections import defaultdict

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        r, l = 0, 0
        m = defaultdict(int)
        res = 0
        while r < len(s):
            m[s[r]] += 1
            str_len = r - l + 1
            if str_len - max(m.values()) <= k:
                print(m)
                if str_len > res:
                    res = str_len
                    print(res)
            else:
                m[s[l]] -= 1
                l += 1
            r += 1
        return res