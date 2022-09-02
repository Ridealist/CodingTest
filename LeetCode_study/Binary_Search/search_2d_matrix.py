"""
https://leetcode.com/problems/search-a-2d-matrix
"""

# Serialization
class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int):
        a = []
        for l in matrix:
            a.extend(l)
        
        l,r = 0, len(a)-1
        while l<=r:
            m = (l+r)//2
            if a[m] == target:
                return True
            elif a[m] > target:
                r = m-1
            else:
                l = m+1
        return False

"""
n * m matrix convert to an array => matrix[x][y] => a[x * m + y]

an array convert to n * m matrix => a[x] =>matrix[x / m][x % m];
"""


## 2D_matrix
## Time Complexity = O(log m*n)
class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int):
        rows, cols = len(matrix), len(matrix[0])
        l,r = 0, rows*cols-1

        while l<=r:
            m = (l+r)//2
            if matrix[m//cols][m%cols] == target:
                return True
            elif matrix[m//cols][m%cols] > target:
                r = m-1
            else:
                l = m+1
        return False