"""
https://leetcode.com/problems/kth-largest-element-in-a-stream/
"""

from heapq import heappush, heappop, heapify, nlargest

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        heapify(nums)
        self.heap = nums

    def add(self, val: int) -> int:
        heappush(self.heap, val)

        for _ in range(self.k):
            res = heappop(self.heap)
        return res


class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = nums
        

    def add(self, val: int) -> int:    
        self.nums.append(val)
        self.nums.sort(reverse=True)
        return self.nums[self.k-1]


# class KthLargest:
#     def __init__(self, k: int, nums: List[int]):
#         # minHeap w/ K largest integers
#         self.minHeap, self.k = nums, k
#         heapq.heapify(self.minHeap)
#         while len(self.minHeap) > k:
#             heapq.heappop(self.minHeap)

#     def add(self, val: int) -> int:
#         heapq.heappush(self.minHeap, val)
#         if len(self.minHeap) > self.k:
#             heapq.heappop(self.minHeap)
#         return self.minHeap[0]