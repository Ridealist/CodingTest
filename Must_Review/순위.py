"""
https://school.programmers.co.kr/learn/courses/30/lessons/49191
"""

import pprint

def solution(n, results):

    # graph = [["?"]*n for _ in range(n)]
    graph = [[0]*n for _ in range(n)]

    for i in range(n):
        # graph[i][i] = "Self"
        graph[i][i] = 0

    for i in results:
        graph[i[1]-1][i[0]-1] = "패" # "Lose"
        graph[i[0]-1][i[1]-1] = "승" # "Win"

    # pprint.pprint(graph)

    for k in range(n):
        for a in range(n):
            for b in range(n):
                # print(k, a, b)
                # 전체탐색을 하는 것으로 graph[a][b] / graph[b][a] 둘 다 처리할 필요 없음!
                if graph[a][k] == "패" and graph[k][b] == "패":
                    graph[a][b] = "패"
                    graph[b][a] = "승"
                elif graph[a][k] == "승" and graph[k][b] == "승":
                    graph[a][b] = "승"
                    graph[b][a] = "패"

    pprint.pprint(graph)

    # return sum("?" not in i for i in graph)
    return len([player for player in graph if player.count(0)==1])
    # return sum(player.count(0)==1 for player in graph)
    # 이런 식도 가능!
    # True: 1 / False: 0 return 하는 것 이용


    
n = 5
results = [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]

solution(n, results)


## 회택풀이
def solution(n, results):
    INF = int(1e9)

    graph = [[INF] * (n + 1) for _ in range(n + 1)]
    for a in range(1, n + 1):
        for b in range(1, n +1):
            if a == b:
                graph[a][b] = 0
    
    for i in range(len(results)):
        graph[results[i][0]][results[i][1]] = 1
        graph[results[i][1]][results[i][0]] = -1
    # pprint(graph)
    for k in range(1, n + 1):
        for a in range(1, n + 1):
            for b in range(1, n + 1):
                if graph[a][k] * graph[k][b] == 1:
                    graph[a][b] = graph[a][k]
                
                
    # pprint(graph)
    answer = 0
    for g in graph:
        count = 0
        count += sum(i == 1 or i == -1 for i in g)
        if count == n - 1:
            answer += 1
    return answer


## 프로그래머스 풀이
# from collections import defaultdict

# def solution(n, results):
#     answer = 0
#     win, lose = defaultdict(set), defaultdict(set)
#     for result in results:
#         lose[result[1]].add(result[0])
#         win[result[0]].add(result[1])