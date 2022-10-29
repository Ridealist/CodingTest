"""
https://school.programmers.co.kr/learn/courses/30/lessons/12945
"""

"""
제한 사항
n은 2 이상 100,000 이하인 자연수입니다.

recursive function은 지나치게 recursion depth가 깊어짐

다른 방법 사용할 필요!
"""

## 1. 하나씩 계산
def solution(n):
    fibo = {0:0, 1:1}
    i = 2
    while i <= n:
        fibo[i] = fibo[i-1] + fibo[i-2]
        i += 1
    return fibo[n] % 1234567

"""
테스트 1 〉	통과 (0.01ms, 10.1MB)
테스트 2 〉	통과 (0.00ms, 10.2MB)
테스트 3 〉	통과 (0.01ms, 10.1MB)
테스트 4 〉	통과 (0.00ms, 10.2MB)
테스트 5 〉	통과 (0.01ms, 10.2MB)
테스트 6 〉	통과 (0.01ms, 10.2MB)
테스트 7 〉	통과 (0.88ms, 10.4MB)
테스트 8 〉	통과 (0.26ms, 10.2MB)
테스트 9 〉	통과 (0.14ms, 10.1MB)
테스트 10 〉	통과 (0.98ms, 10.4MB)
테스트 11 〉	통과 (0.12ms, 10.2MB)
테스트 12 〉	통과 (0.16ms, 10.2MB)
테스트 13 〉	통과 (351.12ms, 464MB)
테스트 14 〉	통과 (346.70ms, 446MB)
"""


## 2. 메모이제이션

import sys
sys.setrecursionlimit(10**8)

memo = {0:0, 1:1}

def solution(n):
    if n in memo:
        return memo[n] % 1234567
    else:
        memo[n] = solution(n-1) + solution(n-2)
        return memo[n] % 1234567

"""
테스트 1 〉	통과 (0.01ms, 10.2MB)
테스트 2 〉	통과 (0.01ms, 10.1MB)
테스트 3 〉	통과 (0.01ms, 10.2MB)
테스트 4 〉	통과 (0.01ms, 10.1MB)
테스트 5 〉	통과 (0.01ms, 10.2MB)
테스트 6 〉	통과 (0.01ms, 10.1MB)
테스트 7 〉	통과 (1.24ms, 11.2MB)
테스트 8 〉	통과 (0.94ms, 10.4MB)
테스트 9 〉	통과 (0.25ms, 10.2MB)
테스트 10 〉	통과 (1.57ms, 11.2MB)
테스트 11 〉	통과 (0.34ms, 10.3MB)
테스트 12 〉	통과 (0.47ms, 10.4MB)
테스트 13 〉	통과 (91.98ms, 97.6MB)
테스트 14 〉	통과 (91.18ms, 95.9MB)
"""