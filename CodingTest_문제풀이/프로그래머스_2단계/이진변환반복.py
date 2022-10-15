"""
https://school.programmers.co.kr/learn/courses/30/lessons/70129
"""

def solution2(s):
    global trans_cnt
    global total_zero
    if s == "1":
        return [trans_cnt,total_zero]
    else:
        total_zero += s.count("0")
        trans_cnt += 1
        return solution2(transform_binary(s))


trans_cnt = 0
total_zero = 0


def transform_binary(s):
    n = "1"*(s.count("1"))
    l = len(n)
    res = bin(l)[2:]
    return res


### 다른 사람 풀이 공부

def solution(s):
    cnt, zero = 0, 0
    while s != "1":
        cnt += 1
        n = s.count("1")
        zero += len(s) - n
        s = bin(n)[2:]
        print(cnt, zero)
        print(s)
    return [cnt, zero]

solution("110010101001")

### 다른 사람 풀이 공부_2

def solution(s):
    from collections import Counter
    cnt, zero = 0, 0
    while s != "1":
        cnt += 1
        counter = Counter(s)
        print(counter)
        zero += counter["0"]
        s = bin(counter["1"])[2:]
    return [cnt, zero]