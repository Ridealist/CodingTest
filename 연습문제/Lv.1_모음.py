"""
https://school.programmers.co.kr/learn/courses/30/lessons/12931
"""

def solution(n):
    return sum([int(i) for i in str(n)])

# map 아이디어
def solution(n):
    return sum(map(int, str(n)))

# 재귀 아이디어
def solution(n):
    if n >= 10:
        r = n % 10
        return r + solution(n // 10)
    return n


"""
https://school.programmers.co.kr/learn/courses/30/lessons/12944
"""

def solution(n):
    return [int(i) for i in list(str(n)[::-1])]

# 좀더 효율적인 풀이!
# list 만들 필요는 없음.
def solution(n):
    return [int(i) for i in str(n)[::-1]]

def solution(n):
    return [i for i in map(int, str(n)[::-1])]

# -> list(map(int, str(n)[::-1]))


# map 객체를 바로 list화 시키는 게 효율적!
def solution(n):
    return list(map(int, reversed(n)))


"""
https://school.programmers.co.kr/learn/courses/30/lessons/12934
"""

def solution(n):
    if int(n**(1/2)) == n**(1/2):
        return (int(n**(1/2))+1)**2
    else:
        return -1

def solution(n):
    sqrt = n ** (1/2)
    if int(sqrt) == sqrt:
        return (sqrt+1)**2
    return -1

def solution(n):
    sqrt = n ** (1/2)
    return (sqrt+1)**2 if int(sqrt) == sqrt else -1


"""
https://school.programmers.co.kr/learn/courses/30/lessons/12933
"""

def solution(n):
    return int("".join(sorted(list(str(n)), reverse=True)))


# 효율화!
# sorted는 안에 iterable이기만 하면 list로 자동 반환해줌!
# sorted(list(str(n)) = sorted(str(n))

def solution(n):
    return int("".join(sorted(str(n), reverse=True)))


# 선택 정렬
def solution(n):
    l = list(str(n))
    n = len(l)
    for i in range(n-1):
        for j in range(i+1, n):
            if l[i] < l[j]:
                l[i], l[j] = l[j], l[i]
    return int("".join(l))

# 삽입 정렬
def solution(n):
    l = list(str(n))
    n = len(l)
    for i in range(1, n):
        for j in range(i, 0 , -1):
            # i가 뒤의 인수, j가 앞의 인수
            # ex) i=1, j=0
            if l[j] > l[j-1]:
                l[j], l[j-1] = l[j-1], l[j]
            else:
                break
    return int("".join(l))