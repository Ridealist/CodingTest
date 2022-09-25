n = 4
m = 5

graph = [
    [0, 0, 1, 1, 0],
    [0, 0, 0, 1, 1],
    [1, 1, 1, 1, 1],
    [0, 0, 0, 0, 0],
]


def dfs(x, y):
    if x < 0 or x >= n or y < 0 or y >= m:
        return  # print("끝")

    if graph[x][y] == 0:
        stack.append((x, y))
        # print("스택: ", stack)
        graph[x][y] = 1
        dfs(x + 1, y)
        dfs(x - 1, y)
        dfs(x, y + 1)
        dfs(x, y - 1)
        return print("완료, ", "스택: ", stack)

    else:
        return  # print("끝")


for i in range(4):
    for j in range(5):
        stack = []
        dfs(i, j)
