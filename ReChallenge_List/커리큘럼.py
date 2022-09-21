"""
입력:
5
10 -1
10 1 -1
4 1 -1
4 3 1 -1
3 3 -1

출력:
10
20
14
18
17
"""

n = int(input())

graph = [[] for i in range(n+1)]
time = [0]*(n+1)
indegree = [0]*(n+1)

for i, _ in enumerate(range(n)):
    l = list(map(int, input().split()))
    time[i+1] = l[0]
    for lec_idx in l[1:]:
        if lec_idx == -1:
            break
        graph[lec_idx].append(i+1)
        indegree[i+1] += 1

print(graph)
print(time)
print(indegree)


from collections import deque

q = deque()

for i in range(1, n+1):
    if indegree[i] == 0:
        q.append(i)

total_time = 0

# while q:
#     # print(q)
#     time_list = []
#     for _ in range(len(q)):
#         now = q.popleft()
#         time_list.append(time[now])
#         for i in graph[now]:
#             indegree[i] -= 1
#             if indegree[i] == 0:
#                 q.append(i)
#     total_time += max(time_list)

total_time = [0] * (n+1)
while q:
    print(q)
    for _ in range(len(q)):
        print(total_time)
        now = q.popleft()
        total_time[now] += time[now]
        for i in graph[now]:
            total_time[i] += total_time[now]
            indegree[i] -= 1
            if indegree[i] == 0:
                q.append(i)


for i in total_time[1:]:
    print(i)
