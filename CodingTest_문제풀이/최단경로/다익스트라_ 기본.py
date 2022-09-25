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
visited = [False] * 7
INF = int(1e9)
distance = [INF] * 7


# import sys
# input = sys.stdin.readline

# n, m = map(int, input().split())
# start = int(input())

# graph = [[] for _ in range(n+1)]
# visited = [False] * (n+1)
# INF = int(1e9)
# distance = [INF] * (n+1)

# for _ in range(m):
#     a, b, c = map(int, input().split())
#     graph[a].append((b, c))

def get_smallest_node():
    min_value = INF
    idx = 0
    for i in range(1, n+1):
        if not visited[i] and distance[i] < min_value:
            min_value = distance[i]
            idx = i
    print(f"탐색 index: {idx}")
    return idx


def dijkstar(start):
    distance[start] = 0
    visited[start] = True
    print(f"탐색 index: {start}")
    for j in graph[start]:
        distance[j[0]] = j[1]

    # 시작 노드를 제외한 전체 n-1개 노드에 대해 반복
    for _ in range(n-1):
        print("노드 탐색 반복횟수:", _)
        # 현재 최단 거리 가장 짧은 노드 꺼내서, 방문 처리
        now = get_smallest_node()
        visited[now] = True

        # 현재 노드와 연결된 다른 노드들 확인
        for next in graph[now]:
            cost = distance[now] + next[1]
            # 현재 노드를 거쳐서 다른 노드로 이동하는 거리가 더 짧은 경우
            if cost < distance[next[0]]:
                distance[next[0]] = cost


dijkstar(start)

# 모든 노드로 가기 위한 최단 거리 출력


for i in range(1, n+1):
    if distance[i] == INF:
        print(f"노드{i}: 도달할 수 없음")
    else:
        print(f"노드{i}:", distance[i])
