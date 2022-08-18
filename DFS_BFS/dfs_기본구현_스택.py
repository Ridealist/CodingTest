graph = [
    [],
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7],
]

visted = [False] * 9

stack = []


def dfs(n):
    if not visted[n]:
        stack.append(n)
        print("스택 추가: ", stack)
        visted[n] = True
        print(n)
        for i in graph[n]:
            dfs(i)
        stack.pop()
        print("스택 제거", stack)


dfs(1)


def dfs(graph, v, visted):
    visted[v] = True
    print(v, end=" ")
    for i in graph[v]:
        if not visted[i]:
            dfs(i)
