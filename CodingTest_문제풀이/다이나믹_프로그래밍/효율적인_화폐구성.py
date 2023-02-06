n, m = map(int, input().split())

array = []
for i in range(n):
    array.append(int(input()))

INF = 9999999

d = [INF] * (m + 1)
d[0] = 0

array.sort()

for i in array:
    for k in range(i, m + 1):
        if d[k - i] != INF:
            d[k] = min(d[k], d[k - i] + 1)

if d[m] == INF:
    print(-1)
else:
    print(d[m])