"""
nums = [0,1,2,3,4,5,6,7,8,9]
5 추가하려고 함
"""
# nums = [0,1,2,3,4,5,6,7,8,9]
# target = 5

# for i in range(len(nums)):
#     if nums[i] >= target:
#         result = i
#         break
# print(f"{i}번째 인덱스에 넣으면 됩니다.")


# 이진탐색 구현
# nums = [0,1,2,3,4,5,6,7,8,9]
# target = 3.6
# l = 0
# r = 9
# while l <= r:
#     m = (l+r)//2
#     if nums[m] == target:
#         print(f"{m}번째 인덱스에 넣으면 됩니다.")
#     elif nums[m] > target:
#         r = m-1
#     else:
#         l = m+1
# if target > nums[m]:
#     print(f"{m+1}번째 인덱스에 넣으면 됩니다.")
# else:
#     print(f"{m-1}번째 인덱스에 넣으면 됩니다.")


# 예제 1
from bisect import bisect_left, bisect_right

nums = [0,1,2,3,4,5,6,7,8,9]
n = 5

print(bisect_left(nums, n))
print(bisect_right(nums, n))


# 예제 2
nums = [4, 5, 5, 5, 5, 5, 5, 5, 5, 6]
n = 5

print(bisect_left(nums, n))
print(bisect_right(nums, n))



## 응용하기 (특정 범위에 속하는 원소의 개수 구하기)

def calCountsByRange(nums, left_value, right_value):
    r_i = bisect_right(nums, right_value)
    l_i = bisect_left(nums, left_value)
    return r_i - l_i

nums = [-1, -3, 5, 5, 4, 7, 1, 7, 2, 5, 6]

# 5 ~ 7 을 갖는 요소의 개수 구하기
nums.sort()  # 정렬은 필수
print(calCountsByRange(nums, 5, 7))

'''
결과값
6
'''