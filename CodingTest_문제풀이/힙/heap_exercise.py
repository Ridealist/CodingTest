"""
https://www.daleseo.com/python-heapq/
"""


from heapq import heappop, heappush, heapify, nlargest, nsmallest

def nth_smallest(nums, n):
    heap = []
    for num in nums:
        heappush(heap, num)
    
    for _ in range(n):
        nth = heappop(heap)
    
    return nth


def nth_smallest(nums, n):
    heapify(nums)

    nth = None
    for _ in range(n):
        nth = heappop(nums)
    
    return nth

print(nth_smallest([4, 1, 7, 3, 8, 5], 3))

nsmallest(3, [4, 1, 7, 3, 8, 5])[-1]
# >>> nsmallest(3, [4, 1, 7, 3, 8, 5])
# [1, 3, 4]

nlargest(1, [4, 1, 7, 3, 8, 5])[-1]