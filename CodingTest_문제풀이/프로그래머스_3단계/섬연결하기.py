"""
https://school.programmers.co.kr/learn/courses/30/lessons/42861
"""

def find_parent(x, table):
    if table[x] != x:
        return find_parent(table[x], table)
    return table[x]


def union(a, b, table):
    a = find_parent(a, table)
    b = find_parent(b, table)
    if a == b:
        return table
    else:
        if a > b:
            table[a] = b
        else:
            table[b] = a
        return table


def solution(n, costs):
    
    table = [i for i in range(n)]
    costs.sort(key=lambda x: x[2])

    answer = 0
    for a,b,cost in costs:
        table = union(a,b,table)
        answer += cost
        print(table)

        if len(set(table)) == 1:
            break
    return answer

n = 4
costs = [[0,1,1],[0,2,2],[1,2,5],[1,3,1],[2,3,8]]

print(solution(n, costs))


#### 회택 풀이

import heapq

def solution(n, costs):
    graph = [[] for _ in range(n)]
    for cost in costs:
        node = cost[0]
        target = cost[1]
        c = cost[2]
        graph[node].append((target, c))
        graph[target].append((node, c))
    
    q = []
    visited = set()
    visited.add(0)
    for i in graph[0]:
        heapq.heappush(q, (i[1], i[0]))
    
    min_cost = 0
    while len(visited) < n:
        weight, node = heapq.heappop(q)
        if node in visited:
            continue

        min_cost += weight
        visited.add(node)
        for i in graph[node]:
            heapq.heappush(q, (i[1], i[0]))
    return min_cost