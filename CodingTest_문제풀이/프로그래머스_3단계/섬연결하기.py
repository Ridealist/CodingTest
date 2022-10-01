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