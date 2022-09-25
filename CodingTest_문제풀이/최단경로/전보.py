import sys
import heapq
from turtle import distance
sys.stdin.readline

n, m, city = map(int, input().split())

INF = int(1e9)
hour = [INF] * (n+1)
graph = [[] for _ in range(n+1)]

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

city_cnt = 0
max_hour = 0

def telegram(start):
    global max_hour
    global city_cnt

    q = []
    heapq.heappush(q, (0, start))
    hour[start] = 0

    while q:
        dist, now = heapq.heappop(q)

        if hour[now] < dist:
            continue

        for pair in graph[now]:
            cost = hour[now] + pair[1]
            if cost > max_hour:
                max_hour = cost
            if cost < hour[pair[0]]:
                hour[pair[0]] = cost
                city_cnt += 1
                heapq.heappush(q, (cost, pair[0]))


telegram(city)

hour_success = [i for i in hour if i != INF]
# total_hour = max(hour_success)
# total_city = len(hour_success) - 1

print(city_cnt, max_hour)

# max = 0
# for i in hour:
#     if i != INF:
#         cnt += 1
#     if i > max:
#         max = i
        
        
###########################3
# 다익스트라 기본 알고리즘 복습

visited = [False] * (n+1)

def get_smallest_node():
    dist = INF
    idx = 0
    for i in range(len(distance)):
        if not visited[i] and distance[i] < dist:
            idx = i
            dist = distance[i]
    return idx

def dijkstrat(start):
    visited[start] = True
    distance[start] = 0

    for next, dist in graph[start]:
        distance[next] = dist

    for _ in range(n-1):
        now = get_smallest_node()
        visited[now] = True

        for next, dist in graph[now]:
            cost = distance[now] + dist
            if cost < distance[next]:
                distance[next] = cost

dijkstrat(start)