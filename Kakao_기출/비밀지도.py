"""
https://school.programmers.co.kr/learn/courses/30/lessons/17681?language=python3
"""

"""
# string은 할당이 안됨
# TypeError: 'str' object does not support item assignment

a = "abcde"
>>> a[0]
a
>>> a[0] = "b"
Error!
"""


def binary(le:int, n:int):
    l = [0 for _ in range(le)]
    idx = le-1
    while n >= 2:
        q, r = divmod(n, 2)
        l[idx] = r
        n = q
        idx -= 1
    l[idx] = n
    # print(l)
    return l

def solution(n, arr1, arr2):
    arr1_mat = [binary(n, i) for i in arr1]
    arr2_mat = [binary(n, i) for i in arr2]
    # print(arr1_mat)

    answer = ["" for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if arr1_mat[i][j] == 1 or arr2_mat[i][j] == 1:
                answer[i] += "#"
            elif arr1_mat[i][j] == 0 and arr2_mat[i][j] == 0:
                answer[i] += " "
    
    return answer


# def solution(n, arr1, arr2):
#     arr1_mat = [binary(n, i) for i in arr1]
#     arr2_mat = [binary(n, i) for i in arr2]
#     # print(arr1_mat)

#     answer = ["#####" for _ in range(n)]

#     for i in range(n):
#         for j in range(n):
#             if arr1_mat[i][j] == 1 or arr2_mat[i][j] == 1:
#                 answer[i][j] == "#"
#             elif arr1_mat[i][j] == 0 and arr2_mat[i][j] == 0:
#                 answer[i][j] == " "
    
#     return answer


solution(5, [9, 20, 28, 18, 11], [30, 1, 21, 17, 28])