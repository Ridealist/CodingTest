"""https://programmers.co.kr/learn/courses/30/lessons/42839?language=python3"""


def makeNumberList(numbers):
    from itertools import permutations

    number_list = []
    for i in range(len(numbers)):
        tuple_list = permutations(numbers, i + 1)
        for tuple in tuple_list:
            num = ""
            for j in range(len(tuple)):
                num += tuple[j]
            number_list.append(int(num))
    number_list = list(set(number_list))
    print(number_list)
    return number_list


# 기본 판별 함수
def is_prime_number(number):
    if number == 0 or number == 1:
        return False
    for i in range(2, number):
        if number % i == 0:
            return False
    return True


def solution(numbers):
    number_list = makeNumberList(numbers)
    answer = 0
    for num in number_list:
        if is_prime_number(num):
            answer += 1
    print(answer)
    return answer


# 제곱근 판별 함수
def is_prime_number(number):
    import math

    if number == 0 or number == 1:
        return False
    for i in range(2, int(math.sqrt(number)) + 1):
        if number % i == 0:
            return False
    return True


# 조합 생성(재귀함수)
def makeCombinations(str1, str2):
    primeSet = set()
    if str1 != "":
        if is_prime_number(int(str1)):
            primeSet.add(int(str1))

    for i in range(len(str2)):
        makeCombinations(str1 + str2[i], str2[:i] + str2[i + 1 :])
    return primeSet


# numbers	return
numbers_1 = "17"
# 3
numbers_2 = "011"
# 2

solution(numbers_2)
