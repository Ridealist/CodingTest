"""
https://school.programmers.co.kr/learn/courses/30/lessons/12935
"""

"""
한줄코딩보다 시,공간 복잡도 우선 고려하기!!!

s1은 min -> O(n), remove -> O(n)
O(2n) 시간 복잡도

s2는 min을 for문 돌 때마다 계속 계산하는 의미에서
O(n**2) 시간 복잡도

s3는 min -> O(n), index -> O(n), pop -> O(n)
O(3n) 시간 복잡도
효율적인 코드는 아님

"""

# s1
def solution(arr):
    arr.remove(min(arr))
    return arr if arr else [-1]

# s2
def solution(arr):
    return [i for i in arr if i > min(arr)] if len(arr) != 1 else [-1]

# s3
def solution(arr):
    arr.pop(arr.index(min(arr)))
    return arr if arr else [-1]