"""
https://codeup.kr/problem.php?id=1916&rid=0
"""

# n = int(input())

# def ffibo(n):
#     if n==1 or n==2:
#         return 1
#     return ffibo(n-1) + ffibo(n-2)

# print(ffibo(n))


# 메모이제이션!
# https://wondytyahng.tistory.com/entry/memoization-메모이제이션
# 지역변수 / 전역변수
# https://rfriend.tistory.com/367


# def fibo_memo(n):
#     # 전역변수 선언
#     global memo
#     if n >= len(memo):
#         memo.append(fibo_memo(n-1) + fibo_memo(n-2))
#     return memo[n]

# memo = [0, 1]

# print(fibo_memo(n))

##########################################################3
"""
https://ssminji.github.io/2020/02/05/the-cake-thief/
"""


def fibo_memo(n):
    # 전역변수 선언
    global memo

    if n in memo:
        print(f"grabbling memo_{n}")
        return memo[n]

    print(f"computing fib_{n}")
    result = fibo_memo(n-1) + fibo_memo(n-2)
    memo[n] = result

    return result

memo = {0:0, 1:1}


print(fibo_memo(5))
print(memo)