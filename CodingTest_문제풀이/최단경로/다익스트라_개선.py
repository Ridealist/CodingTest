n = 6
m = 11
start = 1
# (1,2,2) = (노드1에서 노드2까지 가는 비용2)
graph = [
    [],
    [(2,2), (3,5), (4,1)],
    [(3,3), (4,2)],
    [(2,3), (6,5)],
    [(3,3), (5,1)],
    [(3,1), (6,2)],
    [],
]
INF = int(1e9)
distance = [INF] * 7
# visited가 필요 없음!
# 최단거리가 갱신되면 해당 노드가 q에 들어가게 됨
# q에서 최단거리 반영이 됐는지 비교하여 visited 여부 판별 가능


import heapq

def dijkstra(start):
    # 우선순위 q
    q = []
    # (거리, 노드번호)를 q에 삽입
    # q는 거리순 정렬됨 - 튜플 앞에 원소 기준 정렬
    heapq.heappush(q, (0, start))
    distance[start] = 0
    
    while q:
        dist, now = heapq.heappop(q)
        
        # 해당 노드를 이미 처리한 적 있다면 무시함
        if distance[now] < dist:
            continue
        
        for i in graph[now]:
            cost = dist + i[1]
            # 최단 경로 갱신
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                # 더 짧은 경로 찾은 노드 정보들 우선순위 큐에 넣기
                heapq.heappush(q, (cost, i[0]))
                
dijkstra(start)

for i in range(1, n+1):
    if distance[i] == INF:
        print(f"노드{i}: 도달할 수 없음")
    else:
        print(f"노드{i}:", distance[i])