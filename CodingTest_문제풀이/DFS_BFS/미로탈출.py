from collections import deque
from pprint import pprint

n = 5
m = 6

graph = [
    [1, 0, 1, 0, 1, 0],
    [1, 1, 1, 1, 1, 1],
    [0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1],
]

queue = deque()


dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]


def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    graph
    print((x, y), "방문함", end=" ")

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dr[i]
            ny = y + dc[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                print("실패")
                continue
            if graph[nx][ny] == 0:
                print("벽")
                continue
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[nx][ny] + 1
                queue.append((nx, ny))
                print((nx, ny), "방문함", end=" ")
                graph[nx][ny] = graph[x][y] + 1
    print(queue)
    pprint(graph)
    return queue


print(bfs(0, 0))
