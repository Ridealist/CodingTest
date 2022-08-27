"""
https://codeup.kr/problem.php?id=1905&rid=0
"""


import sys
class recursion_depth:
    def __init__(self, limit):
        self.limit = limit
        self.default_limit = sys.getrecursionlimit()
    def __enter__(self):
        sys.setrecursionlimit(self.limit)
    def __exit__(self, type, value, traceback):
        sys.setrecursionlimit(self.default_limit)


n = input()
n = int(n)

def sum(n):
    if n == 1:
        return n
    return n + sum(n-1)

# print(sum(n))


with recursion_depth(20000):
    print(sum(n))

################################################

import sys
sys.setrecursionlimit(1000000)

n = input()
n = int(n)

def sum(n):
    if n > 1:
        return n + sum(n-1)
    return n

print(sum(n))

###############################################


from functools import reduce

reduce(lambda x,y: x+y, range(n), 0)