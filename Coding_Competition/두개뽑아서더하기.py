"""
https://school.programmers.co.kr/learn/courses/30/lessons/68644
"""

# generator
# 생성자, yield를 통한 문법
# next()를 통해 값 계속 생성 가능
# 무한루프도 만들 수 있음!
"""
Generator()
https://wikidocs.net/16069
"""

"""
https://twpower.github.io/120-python-in-operator-time-complexity

in 시간 복잡도
list, tuple -> O(n)

set, dict -> O(1), 최악:O(n)
"""

import itertools


def solution(numbers):
    return sorted(set([sum(i) for i in itertools.combinations(numbers, 2)]))


def solution1(numbers):
    comb = itertools.combinations(numbers, 2)
    answer = set()
    for pair in comb:
        answer.add(sum(pair))
    return sorted(answer)


def solution2(numbers):
    result = set()
    for idx, i in enumerate(numbers):
        for j in numbers[idx + 1 :]:
            result.add(i + j)
    answer = sorted(result)
    return answer


def test_generator():
    cnt = 0
    re = [1, 2, 3]
    while True:
        yield re[cnt % 3]
        cnt += 1


def three_generator():
    a = [1, 2, 3]
    for i in a:
        yield i
