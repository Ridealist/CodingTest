# 집의 개수:n , 길의 개수:m
def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


n, m = map(int, input().split())

parent = [i for i in range(n+1)]
total_cost = 0
cost_list = []
graph = []
## edge = [] 변수 이름 활용 good!
## 간선 정보를 담을 리스트

for _ in range(m):
    a, b, cost = map(int, input().split())
    graph.append((cost, a, b))

graph.sort()
### last = 0

print(graph)

for cost, a, b in graph:
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        total_cost += cost
        cost_list.append(cost)
        ### last = cost
        print((cost, a, b))

print(total_cost - cost_list[-1])
### print(total_cost - last)

"""
입력:
7 12
1 2 3
1 3 2
3 2 1
2 5 2
3 4 4
7 3 6
5 1 5
1 6 2
6 4 1
6 5 3
4 5 3
6 7 4

출력: 8
"""
