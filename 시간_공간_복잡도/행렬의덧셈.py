"""
https://school.programmers.co.kr/learn/courses/30/lessons/12950
"""

"""
연산 10억번(1,000,000,000) C언어 기준 1초 정도 소요
보통 연산횟수 10억번 이상이면 오답 판정 받을 수...

N = 100일 때 연산 횟수

O(N)     -> 1,000
O(NlogN) -> 10,000
O(N**2)  -> 1,000,000
O(N**3)  -> 1,000,000,000 
"""

"""
# 시간 제한이 1초일 때, 시간복잡도 기준!

N <= 500             -> O(N**3)인 알고리즘 설계 가능
N <= 2,000           -> O(N**2)
N <= 100,000    십만 -> O(NlogN)
N <= 10,000,000 천만 -> O(N)
N <= 10,000,000,000 백억  -> O(logN)
"""


def solution(arr1, arr2):
    row, col = len(arr1), len(arr1[0])
    mat = [[0 for _ in range(col)] for _ in range(row)]
    for i in range(row):
        for j in range(col):
            mat[i][j] = arr1[i][j] + arr2[i][j]
    return mat


# 2차원 행렬 좀 더 효율적으로 만들기!
# 바깥쪽 for 문에 row 정보, 안쪽 for 문에 col 정보 넣고 하나씩 돌리기
def solution(arr1, arr2):
    answer = [[arr1[i][j] + arr2[i][j] for j in range(len(arr1[0]))] for i in range(len(arr1))]
    return answer


# zip 함수 이용!
def solution(arr1, arr2):
    return [[sum(i) for i in zip(a1, a2)] for a1, a2 in zip(arr1, arr2)]

