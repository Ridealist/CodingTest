"""
https://www.acmicpc.net/problem/12865

참고 블로그
https://jeonyeohun.tistory.com/86

"""
# TODO 전형적 DP 문제 공부! 
n, k = map(int, input().split())

bag = []
d = [[0] * (k + 1) for i in range(n + 1)]

weight = 0
value = 1

for i in range(n):
    w, v = map(int, input().split())
    bag.append((w, v))

# d를 생성할 때 0으로 초기화 했으므로 불필요한 코드
# for w in range(k):
#     d[0][w] = 0

for i in range(1, n + 1):
    # d를 생성할 때 0으로 초기화 했으므로 불필요한 코드
    # d[i][0] = 0
    for w in range(1, k + 1):
        if bag[i - 1][weight] <= w:
            d[i][w] = max(d[i - 1][w], d[i - 1][w - bag[i - 1][weight]] + bag[i - 1][value])
        else:
            d[i][w] = d[i - 1][w]

print(d[n][k])