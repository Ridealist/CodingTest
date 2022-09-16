import time

start_time = time.time()

# def find_parent(parent, x):
#     if parent[x] != x:
#         # print(f"parent 한번 더 찾기: {x} -> {parent[x]}")
#         return find_parent(parent, parent[x])
#     # print("찾았다:", x)
#     return x


# 경로 압축 기법 코드
def find_parent(parent, x):
    if parent[x] != x:
        print(f"parent 한번 더 찾기: {x} -> {parent[x]}")
        parent[x] = find_parent(parent, parent[x])
    print("찾았다:", parent[x])
    return parent[x]


# parent = [None, 1, 1, 2, 1, 5, 5]

# find_parent(parent, 3)


def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

# 노드의 갯수 v, 간선의 갯수 e
v, e = map(int, input().split())
parent = [0] * (v + 1)

# 부모 테이블상에서, 부모를 자기 자신으로 초기화
for i in range(1, v + 1):
    parent[i] = i

# union 연산 각각 수행
for i in range(e):
    a, b = map(int, input().split())
    union_parent(parent, a, b)

# 각 원소가 속한 집합 출력
print("각 원소가 속한 집합: ", end="")
for i in range(1, v + 1):
    print(find_parent(parent, i), end=" ")

print()

# 부모 테이블 내용 출력
print("부모 테이블: ", end="")
for i in range(1, v + 1):
    print(parent[i], end=" ")

end_time = time.time()
print("time: ", end_time - start_time)