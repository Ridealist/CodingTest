from typing import List

def search(nums: List[int], target: int):
    left = 0
    right = len(nums)-1

    while left <= right:
        pivot = (left + right)//2
        if nums[pivot] == target:
            print("찾았다!")
            return pivot
        if nums[pivot] > target:
            print("못찾았다. 오른쪽 바운더리 이동")
            right = pivot - 1
        else:
            print("못찾았다. 왼쪽 바운더리 이동")
            left = pivot + 1
    return -1

nums = [1,2,3,4,5,6,7,8,9]
target = 10

print(search(nums, target))

n = 5 # 데이터 갯수
m = 5 # 부분합 M
# data = List[int]
data = [1,2,3,4,5]

cnt = 0 # 부분합이 M이 되는 갯수
subs = data[0] # 중간중간 구간합
end = 0

for start in range(n):
    # s = sum(data[start:end+1]) # sum() -> O(k) iterable 돌면서 sum variable에 합치는 것
    while subs < m and end < n:
        print(f"아직... 부분합: {subs}, start={start}, end={end}")
        end += 1
        subs += data[end]
    if subs == m:
        print(f"찾았다, start={start}, end={end}")
        cnt += 1
    subs -= data[start]

print(cnt)

import time
import random

# random.randint(0,2)

nums = [random.randint(0,2) for _ in range(10000)]


start_time = time.time()
def sortColors(nums=List[int]):
    z_point = 0
    t_point = len(nums)-1
    point = 0

    while point <= t_point:
        if nums[point] == 0:
            nums[z_point], nums[point] = nums[point], nums[z_point]
            z_point += 1
        elif nums[point] == 2:
            nums[t_point], nums[point] = nums[point], nums[t_point]
            t_point -= 1
            if nums[point] == 0:
                nums[z_point], nums[point] = nums[point], nums[z_point]
                z_point += 1
        point += 1

    return nums
end_time = time.time()

print("쓰리포인터 성능 측정:", end_time-start_time)

nums = []
nums = [random.randint(0,2) for _ in range(10000)]

start_time = time.time()
nums.sort()
end_time = time.time()

print("파이썬 기본 정렬 성능 측정:", end_time-start_time)

# print(sortColors([1,0,2,2,0,1,2,1,0]))