from collections import deque

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

queue = deque()

visted = [False] * 9


def bfs(n):
    queue.append(n)
    print("큐: ", queue)
    visted[n] = True
    print(n)

    while queue:
        pop = queue.popleft()
        print("큐 삭제: ", pop)
        for i in graph[pop]:
            if not visted[i]:
                queue.append(i)
                print("큐: ", queue)
                visted[i] = True
                print(i)


bfs(1)
