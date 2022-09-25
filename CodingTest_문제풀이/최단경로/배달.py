"""
https://school.programmers.co.kr/learn/courses/30/lessons/12978
"""

N = 5
road = [[1,2,1],[2,3,3],[5,2,2],[1,4,2],[5,3,1],[5,4,2]]

import heapq

INF = int(1e9)

# 그래프 만드는 방법 순서는 상관 없음!
# (거리, 도시) / (도시, 거리) 무관!
def makegraph(N, road):
    graph = [[] for _ in range(N+1)]
    for c1, c2, dist in road:
        graph[c1].append((c2, dist))
        graph[c2].append((c1, dist))
    return graph

print(makegraph(N, road))


def solution(N, road, K):

    graph = makegraph(N, road)
    distance = [INF]*(N+1)

    q = []
    # heapq에서만 (거리, 도시) 기준으로 집어넣어 주면 됨.
    heapq.heappush(q, (0, 1))
    distance[1] = 0
    
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for city, dist in graph[now]:
            cost = distance[now] + dist
            if cost < distance[city]:
                distance[city] = cost
                heapq.heappush(q, (cost, city))

    return len([i for i in distance if i <= K])


# 다른 사람 풀이 공부
def solution(N, road, K):
    visited = [False] * (N+1)
    costs = [float('inf')] * (N+1)
    costs[1] = 0
    parents = [1]

    while (parents):
        parent = parents.pop(0)
        visited[parent] = True

        for a, b, cost in road:
            if a == parent or b == parent:
                target = b if a == parent else a
                c = costs[parent] + cost
                if c < costs[target]:
                    costs[target] = c
                    parents.append(target)

    return sum(1 for c in costs if c<=K)



# 다른 사람 풀이 참조
# 기본 다익스트라 알고리즘 동일
def solution(N, road, K):
    visted = [False] * (N+1)
    D = [INF] * (N+1)
    r = [[(None, None)]] + [[] for _ in range(N)]

    for c1, c2, dist in road:
        r[c1].append((c2, dist))
        r[c2].append((c1, dist))
    
    D[1] = 0
    
    for _ in range(1, N+1):
        min_cost = INF

        # 다음 방문 노드 찾기 로직
        m = None
        for i in range(1, N+1):
            if not visted[i] and D[i] < min_cost:
                min_cost = D[i]
                m = i
        visted[m] = True

        for city, dist in r[m]:
            cost = D[m] + dist
            if cost < D[city]:
                D[city] = cost

    return len([d for d in D if d<=K])