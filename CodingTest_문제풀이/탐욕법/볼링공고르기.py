# 공 개수 n / 공 최대 무게 m
n, m = map(int, input().split())

boal = list(map(int, input().split()))

dic_boal = {i:0 for i in range(1, m+1)}

# print(dic_boal)

for i in boal:
    dic_boal[i] += 1

answer = 0
sub = 0
for i in range(1, m+1):
    sub += dic_boal[i]
    answer += dic_boal[i] * (n - sub)

print(answer)


## 책 풀이 공부
n, m = map(int, input().split())

boal = list(map(int, input().split()))

weight = [0]*11

for i in boal:
    weight[i] += 1

res = 0
n = len(boal)
for i in range(1, m+1):
    n -= weight[i]
    res += weight[i] * n

print(res)


## Combination 풀이
## Brute Force 두려워 말고 항상 연습해놓기!
from itertools import combinations

n, m = map(int, input().split())

boal = list(map(int, input().split()))

cnt = 0
for a, b in combinations(boal, 2):
    if a != b:
        cnt += 1

print(cnt)


###
## 인덱스로도 풀어보기!!!