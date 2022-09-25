"""
https://school.programmers.co.kr/learn/courses/30/lessons/12900
"""

"""
s1
튜플 패킹(packing)과 언패킹(unpacking)을 이용, 두 값을 반복문에서 지속적으로 변경하며 값 구함
가독성이 떨어지나 가장 효율적인 연산
O(n)

s2
수학점 점화식과 비슷한 형태, 가독성 높아짐
but! 연산 효율이 떨어지는 단점! -> 인덱스 숫자가 높아질수록 연산 효율 급격한 저하

## import sys
## print(sys.getrecursionlimit())
   -> 재귀 최대 깊이 확인
## sys.setrecursionlimit(limit)
   -> 재귀 최대 깊이 설정

s3
메모이제이션: 이미 연산했던 값은 더 이상 연산하지 않도록 기록 -> 불필요한 연산을 제거하여 효율성 up
n번째 피보나치 수를 구하는 함수의 연산 횟수는 (n * 2 - 3) 번

"""

fibo = 15


# s1 기본 for문 활용
count = 0

def fibo_forloop(n):
    global count
    _cur, _next = 1, 2
    for i in range(1, n+1):
        count += 1
        print(f"for loop[{i}] _cur:{_cur}, _next:{_next}, count: {count}")
        if i >= 2:
            _cur, _next = _next, _cur + _next
    print(f"결과: {_cur}", "\n")
    return _cur

fibo_forloop(fibo)


# s2 재귀함수
count = 0

def fibo_recur(n):
    global count
    count += 1
    print(f'fibo_recur({n}) 호출, count: {count}')
    if n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        return fibo_recur(n-1) + fibo_recur(n-2)

print(f"결과:", fibo_recur(fibo), "\n")

# s3 재귀함수 + 메모이제이션
count = 0
memo = {
    1: 1,
    2: 2
}

def fibo_memo(n):
    global count
    count += 1
    print(f'fibo_memo({n}) 호출, count: {count}')
    if n in memo:
        return memo[n]
    else:
        memo[n] = fibo_memo(n-1) + fibo_memo(n-2)
        print(memo)
        return memo[n]

print(f"결과:", fibo_memo(fibo), "\n")