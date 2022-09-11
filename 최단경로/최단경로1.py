"""
https://codeup.kr/problem.php?id=3215
"""

import sys
import string
import heapq

f = open("C:/Users/Junbo Koh/Desktop/CodingTest/최단경로/codeup.txt", 'r')
lines = f.readlines()

# sys.stdin.readline
INF = int(1e9)

# for line in lines:
#     line = line.strip()
#     n, m = map(int, line.split())

line = lines[0].strip()
n, m = map(int, line.split())

# 노드 갯수 n / 노드 사이 잇는 간선 갯수 m
# n, m = map(int, input().split())
alpha_up = string.ascii_uppercase

distance = {alpha_up[i]:INF for i in range(n)}
graph = {alpha_up[i]:[] for i in range(n)}


for l in lines[1: m+1]:
    l = l.strip()
    a, b, c = l.split()
    graph[a].append((b, int(c)))
    ### 방향성이 있는 그래프가 아니면!!! 상호 저장해주어야 함!!!
    graph[b].append((a, int(c)))


# for _ in range(m):
#     a, b, c = input().split()
#     graph[a].append((b, int(c)))

line = lines[-1].strip()
start, end = line.split()

# start, end = input().split()

# print(graph)

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        dist, node = heapq.heappop(q)
        
        if distance[node] < dist:
            continue

        for pair in graph[node]:
            cost = dist + pair[1]
            if cost < distance[pair[0]]:
                distance[pair[0]] = cost
                heapq.heappush(q, (cost, pair[0]))
                print(q)


dijkstra(start)

if distance[end] == INF:
    print(-1)
else:
    print(distance[end])