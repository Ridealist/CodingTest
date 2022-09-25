"""
https://leetcode.com/problems/valid-anagram/submissions/
"""


class Solution:
    def isAnagram(self, s: str, t: str):
        sl = [i for i in s]
        tl = [i for i in t]
        sl.sort()
        tl.sort()
        if sl == tl:
            return True
        else:
            False


class Solution:
    def isAnagram(self, s: str, t: str):
        sl = [i for i in s]
        tl = [i for i in t]
        if set(sl) != set(tl):
            return False
        else:
            sl.sort()
            tl.sort()
            if sl == tl:
                return True
            else:
                False


class Solution:
    def isAnagram(self, s: str, t: str):
        if len(s) != len(t):
            return False

        countS, countT = {}, {}

        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)
        return countS == countT


def isAnagram(s, t):
    if len(s) != len(t):
        return False

    countS, countT = {}, {}

    for i in range(len(s)):
        countS[s[i]] = 1 + countS.get(s[i], 0)
        countT[t[i]] = 1 + countT.get(t[i], 0)

    return countS == countT
