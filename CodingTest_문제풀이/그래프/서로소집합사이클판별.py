def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


# 원소 합치기
def union(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a > b:
        parent[a] = b
    else:
        parent[b] = a

# 노드 갯수, 간선 갯수
v, e = map(int, input().split())

# 자기 자신을 부모로하는 테이블로 초기화
parent = [i for i in range(v+1)]

cycle = False

for i in range(e):
    a, b = map(int, input().split())
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a == b:
        cycle = True
        break
    else:
        union(parent, a, b)

if cycle:
    print("사이클이 발생했습니다.")
else:
    print("사이클이 발생하지 않았습니다.")
