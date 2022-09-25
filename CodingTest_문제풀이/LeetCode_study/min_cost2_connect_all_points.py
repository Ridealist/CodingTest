"""
https://leetcode.com/problems/min-cost-to-connect-all-points/
"""

"""
union find -> 깊이가 깊지 않은 tree 만드는게 핵심!!!

https://bowbowbow.tistory.com/26


크루스칼
heap pop -> log(V**2)
파이썬 기본 sort -> V * log(V)
"""


from itertools import combinations
from typing import List

class Solution:
    
    def calcost(self, p1: list, p2: list):
        return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])
    
    def get_parent(self, parent: dict, x: list):
        if parent[str(x)] != x:
            parent[str(x)] = self.get_parent(parent, parent[str(x)])
        return parent[str(x)]
    
    def union(self, parent, p1, p2):
        p1 = self.get_parent(parent, p1)
        p2 = self.get_parent(parent, p2)
        if abs(p1[0]) + abs(p1[1]) > abs(p2[0]) + abs(p2[1]):
            parent[str(p1)] = p2
        else:
            parent[str(p2)] = p1
        
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        edge = []
        parent = {}
        
        for point in points:
            parent[str(point)] = point
        
        for p1, p2 in combinations(points, 2):
            edge.append((self.calcost(p1, p2), p1, p2))
        
        edge.sort()
        result = 0
        
        for cost, p1, p2 in edge:
            if self.get_parent(parent, p1) != self.get_parent(parent, p2):
                self.union(parent, p1, p2)
                result += cost
                # print(cost, p1, p2)
                # print(parent)
        
        return result


5 [16, -18] [13, -20]
12 [-8, 14] [-15, 9]
13 [-18, 19] [-15, 9]
20 [-19, -13] [-4, -8]
26 [-19, -13] [-15, 9]
26 [-8, 14] [-4, -8]
29 [13, -20] [-4, -8]
34 [-8, 14] [20, 20]

{'[-8, 14]': [-4, -8], '[16, -18]': [-4, -8], '[-19, -13]': [-4, -8], '[-18, 19]': [-4, -8], '[20, 20]': [-4, -8], '[13, -20]': [-4, -8], '[-15, 9]': [-4, -8], '[-4, -8]': [-4, -8]}
