"""
https://school.programmers.co.kr/learn/courses/30/lessons/12917?language=python3
"""

## "구분자".join(리스트)
"""
arr = ['가', '나', '다', '라', "BlockDMask", '마']
print(arr)

# 그냥 하나의 문자열로 합쳐버리기
str = ''.join(arr)
print(str)

가나다라BlockDMask마
"""

from functools import reduce

def solution(s):
    list_s = list(s)
    list_s.sort(reverse=True)
    return reduce(lambda x,y: x+y, list_s, "")


def solution(s):
    return "".join(sorted(list(s), reverse=True))

## 선택 정렬 이용
def solution(s):
    s = list(s)
    n = len(s)
    for i in range(n-1):
        for j in range(i+1, n):
            if ord(s[i]) < ord(s[j]):
                s[i], s[j] = s[j], s[i]
    return "".join(s)

## 삽입 정렬 이용
def solution(s):
    s = list(s)
    n = len(s)
    for i in range(1, n):
        for j in range(i, 0, -1):
            if ord(s[j]) > ord(s[j-1]):
                s[j], s[j-1] = s[j-1], s[j]
            else:
                break
    return "".join(s)