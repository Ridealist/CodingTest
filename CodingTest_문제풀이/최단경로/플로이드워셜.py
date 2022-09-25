INF = int(1e9)

f = open("C:/Users/Junbo Koh/Desktop/CodingTest/최단경로/플로이드워셜_교재.txt", 'r')
lines = f.readlines()

lines[0] = 

# 노드 갯수 n / 간선 갯수 m
n = int(input())
m = int(input())

# n = 5
# m = 6

graph = [[INF]*(n+1) for _ in range(n+1)]

# 자기 자신에서 자기 자신으로 가는 비용 0으로 초기화
for i in range(1, n+1):
    graph[i][i] = 0

# for a in range(1, n+1):
#     for b in range(1, n+1):
#         if a == b:
#             graph[a][b] = 0

# 각 간선 정보 입력받아, 값 초기화
for _ in range(m):
    # A에서 B로 가는 비용 C
    a, b, c = map(int, input().split())
    graph[a][b] = c

for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            if a == k or b == k:
                continue
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

for a in range(1, n+1):
    for b in range(1, n+1):
        # 도달할 수 없는 경우 '무한'으로 출력
        if graph[a][b] == INF:
            print("INFINITY", end=" ")
        else:
            print(graph[a][b], end=" ")
    print()
