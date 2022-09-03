"""
https://leetcode.com/problems/koko-eating-bananas/submissions/
"""


"""
math.ceil -> 올림
math.trunc -> 내림
  == int

round(x, n) -> 반올림

round()는 사사오입 원칙을 따른다. 반올림할 자리의 수가 5이면 반올림 할 때 앞자리의 숫자가 짝수면 내림하고 홀수면 올림 한다.
>>> round(4.5)  #결과는 4
>>> round(3.5)  #결과는 4
앞의 자리가 4인 경우 짝수니까 내림이 되었고 앞의 자리가 3인 경우 홀수니까 올림이 적용되었다.

"""

import math

class Solution:
    def minEatingSpeed(piles: list[int], h: int):
        l = 1
        r = max(piles)
        # result = 0
        print(f"첫시작점: {l}, 첫끝점: {r}")
        while l<=r:
            m = (l+r)//2
            s = sum([math.ceil(p/m) for p in piles])
            # 올림 안쓰는 방법도 공부!
            # s = sum([p-1//m + 1 for p in piles])
            print(f"중간점: {m}, 목표값: {h}, 현재 걸리는 시간: {s}")
            if s <= h:
                # result = m
                r = m-1
                # print(f"임시결과: {result}")
            else:
                l = m+1
        return m

piles = [30,11,23,4,20]
h = 6

print(Solution.minEatingSpeed(piles=piles, h=h))

"""
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low, high = 1, max(piles)
        # result = 0
        while low <= high:
            mid = (low + high) // 2
            print(mid)
            if not self.isInTime(piles, h, mid):
                low = mid + 1
            else:
                # result = mid
                high = mid - 1
        return mid #result
    
    def isInTime(self, piles, h, mid):
        s = 0
        for i in piles:
            s +=  (i - 1) // mid + 1
        return s <= h
"""
### 회택 풀이
