"""
https://www.acmicpc.net/problem/2437
"""

n = int(input())
coins = list(map(int, input().split()))

coins.sort()

target = 1
for x in coins:
    if target < x:
        break
    else:
        target += x

print(target)


## 백준 풀이-1
import sys

N = int(sys.stdin.readline())
W = sorted(list(map(int, sys.stdin.readline().split())))

if W[0] != 1:
	print(1)
else:
	answer = None
	total = W[0]
	for w in W[1:]:
		if w <= total + 1:
			total += w
		else:
			answer = total + 1
			break
	if answer is None:
		answer = total + 1

	print(answer)


## 백준 풀이 - 2
N = int(input())
choo = list(map(int, input().split()))

choo.sort()
ans = 0
i = 0
while i < N:
    if ans + 1 < choo[i]:
        break
    ans += choo[i]
    i += 1
ans += 1
print(ans)
