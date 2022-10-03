"""
https://school.programmers.co.kr/learn/courses/30/lessons/60059
"""


def makemap(n, m, lock):
    l = 2 * m + n
    Map = [[0 for _ in range(l)] for _ in range(l)]
    
    for i in range(n):
        for j in range(n):
            Map[m+i][m+j] = lock[i][j]

    return Map

key = [[0, 0, 0], [1, 0, 0], [0, 1, 1]]
lock = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]

m = makemap(len(key[0]), len(lock[0]), lock)

import pprint

pprint.pprint(m)



def lotate_once(key):
    new_key = []
    for i in range(len(key[0])):
        l = []
        for j in range(len(key)-1, -1, -1):
            l.append(key[j][i])
        new_key.append(l)
    print("키 변경: ", new_key)
    return new_key


def solution(key, lock):
    m = len(key[0])
    n = len(lock[0])

    for _ in range(4):
        # 위치 옮겨가면서 키 끼우기
        for i in range(1, m+n):
            for j in range(1, m+n):
                Map = makemap(n, m, lock)
                for idx in range(m):
                    for jdx in range(m):
                        Map[i+idx][j+jdx] += key[idx][jdx]

                # Map을 update 한 후 딱 맞는지 확인
                # print(i, j)
                part = [i[n:n+m] for i in Map[n:n+m]]
                # print("중간 단계:", part)
                flag = True
                for u in range(m):
                    for v in range(m):
                        if part[u][v] != 1:
                            flag = False
                if flag:
                    return True
        
        # 전체 경우에 대해 모두 True 아니면 키 돌리기
        key = lotate_once(key)
    
    return False

solution(key, lock)


# print(lotate([[0, 0, 0], [1, 0, 0], [0, 1, 1]]))
# print(lotate([[0, 1, 0], [1, 0, 0], [1, 0, 0]]))

