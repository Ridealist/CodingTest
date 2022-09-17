# 특정 원소가 속한 집합 찾기
# 루트 노드가 아니면 루트 노드를 찾을 때까지 재귀적으로 호출
def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

# 두 원소가 속한 집합 합치기
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a > b:
        parent[a] = b
    else:
        parent[b] = a

# 노드 갯수, 간선 갯수
v, e = map(int, input().split())

# 부모 테이블, 부모 자기 자신으로 초기화
parent = [i for i in range(v+1)]


## 크루스칼 핵심!! ##
# 모든 간선을 담을 리스트와 최종 비용을 담을 변수
edges = []
result = 0

# 모든 간선에 대한 정보 입력받기
for _ in range(e):
    a, b, cost = map(int, input().split())
    edges.append((cost, a, b))

# 간선을 비용 순으로 정렬
edges.sort()

# 간선을 하나씩 확인하며
for cost, a, b in edges:
    # 사이클이 발생하면 집합에 불포함
    if find_parent(parent, a) == find_parent(parent, b):
        continue
    else:
        union_parent(parent, a, b)
        result += cost

print(result)
print(parent)

7 9
1 2 29
1 5 75
2 3 35
2 6 34
3 4 7
4 6 23
4 7 13
5 6 53
6 7 25

>>> 159
>>> [0, 1, 1, 1, 3, 1, 1, 3]