from collections import deque

n = 5
m = 5
cnt = 0

graph = [
    [1, 0, 1, 1, 1],
    [1, 0, 1, 0, 1],
    [1, 0, 1, 1, 1],
    [1, 1, 1, 0, 1],
    [0, 0, 0, 0, 1],
]

queue = deque()


dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]


def bfs(x, y):
    x = 0
    y = 0

    while x == n and y == m:

        for i in range(4):
            x += dr[i]
            y += dr[i]
            if x < 0 or x >= n or y < 0 or y >= m:
                print("실패")

            if graph[x][y] == 1:
                graph[x][y] = 0
                queue.append()
                print((x, y), "방문함")

        if x == n - 1 and y == m - 1:
            print("도착")
            return
    else:
        print("실패")
        return


print(bfs(0, 0))
