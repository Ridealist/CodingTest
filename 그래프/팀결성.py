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

# union = []
# check = []

# for _ in range(m):
#     # 연산의 의미 'oper' 변수 할당!!!
#     oper, a, b = map(int, input().split())
#     if oper == 0:
#         union.append((a, b))
#     else:
#         check.append((a, b))


### 문제 의도에 맞는 풀이
for _ in range(m):
    # 연산의 의미 'oper' 변수 할당!!!
    oper, a, b = map(int, input().split())
    if oper == 0:
        union_parent(parent, a, b)
    else:
        if find_parent(parent, a) == find_parent(parent, b):
            print("YES")
        else:
            print("NO")


# for a, b in union:
#     union_parent(parent, a, b)

# print(union)
# print(check)
print(parent)

# for a, b in check:
#     if parent[a] == parent[b]:
#         print("YES")
#     else:
#         print("NO")
        
"""
7 8
0 1 3
1 1 7
0 7 6
1 7 1
0 3 7
0 4 2
0 1 1
1 1 1
"""

