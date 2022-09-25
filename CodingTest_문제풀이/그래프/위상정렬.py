from collections import deque

v, e = map(int, input().split())

# 진입차수 : 특정한 노드로 '들어오는' 간선의 갯수
# 모든 노드에 대한 진입차수 0으로 초기화
indegree = [0] * (v+1)

# 각 노드에 연결된 간선 정보를 담기 위한 연결 리스트(그래프) 초기화
graph = [[] for i in range(v+1)]

# 방향 그래프의 간선 정보 입력받기
for _ in range(e):
    a, b = map(int, input().split())
    # 정점 A에서 B로 이동 가능
    graph[a].append(b)
    # B 진입차수 1 증가
    indegree[b] += 1

def topology_sort():
    result = []
    q = deque()

    # 처음 시작할 때 진입차수 0인 노드 큐에 삽입
    for i in range(1, v+1):
        if indegree[i] == 0:
            q.append(i)

    while q:
        node = q.popleft()
        result.append(node)
        # 해당 원소와 연결된 노드들의 진입차수 1 빼기
        for i in graph[node]:
            indegree[i] -= 1
            # 새롭게 진입차수 0이 도는 노드 큐에 삽입
            if indegree[i] == 0:
                q.append(i)

    for i in result:
        print(i, end=" ")

topology_sort()


7 8
1 2
1 5
2 3
2 6
3 4
4 7
5 6
6 4