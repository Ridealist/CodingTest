"""
https://school.programmers.co.kr/learn/courses/30/lessons/68935
"""

"""
# python operator
## 산술 연산자(arithmetic operator)
# +, -, *, /, %(나머지), //(몫), **(거듭제곱)

## 할당 연산자(assignment operator)
# =, +=, -=, *=, /=

## 비트 연산자(bitwise operator)
&: 둘다 참일때 만족,
|: 둘 중 하나만 참이여도,
^: 둘 중 하나만 참일 때

"""

# 진법 변환!
# int(value, n) -> n 진법으로 value값 변환!

# 몫 나머지 한번에 계산!
# (q, r): tuple = divmod(m, n) -> 몫 q(quotient), 나머지 r(remainder) 튜플로 반환

# list(str()) = 각각의 원소인 list
# list("abc") ["a", "b", "c"]

# 뒤에 있는 원소 가져오고 싶다
# list.pop() 고려! (선입후출 구조)


def solution1(n):
    remain = []
    while n >= 3:
        r = n % 3
        remain.append(r)
        n = n // 3
    remain.append(n)
    answer = 0
    i = 0
    # for i, v in enumerate(remain):
    #     answer += v * 3 ** (len(remain) - 1 - i)
    while remain:
        v = remain.pop()
        answer += v * 3**i
        i += 1
    print(answer)
    return answer


# 클래스비누
def solution(n):
    remain = []
    while n >= 3:
        r = n % 3
        remain.append(str(r))
        n = n // 3
    remain.append(str(n))

    num = "".join(remain)
    answer = int(num, 3)
    print(answer)


# 은섭형
def convert_to_ternary(n):
    if n == 0:
        return "0"
    nums = []
    while n:
        n, r = divmod(n, 3)
        nums.insert(0, str(r))
    nums = nums[::-1]
    num = "".join(nums)
    print(num)
    return num


def convert_to_decimal(n: str):
    nums = []
    n = list(n)
    i = 0
    while n:
        nums.append(int(n.pop()) * (3**i))
        i += 1
    return sum(nums)


def solution(n):
    answer = 0
    # convert to ternary
    # filp it
    ternary = convert_to_ternary(n)
    # conver to decimal

    return convert_to_decimal(ternary)
