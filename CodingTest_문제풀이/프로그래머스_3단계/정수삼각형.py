"""
https://school.programmers.co.kr/learn/courses/30/lessons/43105
"""

def solution(triangle):
    for i in range(len(triangle)-1):
        triangle[i+1][0] += triangle[i][0]
        triangle[i+1][-1] += triangle[i][-1]
        for j in range(1, len(triangle[i+1])-1):
            M = max(triangle[i][j-1], triangle[i][j])
            triangle[i+1][j] += M
    
    return max(triangle[-1])

### 다른 사람 풀이 공부

def solution(triangle):
    for t in range(1, len(triangle)):
        for i in range(t+1):
            if i == 0:
                triangle[t][0] += triangle[t-1][0]
            elif i == t:
                triangle[t][-1] += triangle[t-1][-1]
            else:
                triangle[t][i] += max(triangle[t-1][i-1], triangle[t-1][i])
    return max(triangle[-1])


### 아래에서 위로

def solution(triangle):
    height = len(triangle)
    
    while height > 1:
        for i in range(height-1):
            triangle[height-2][i] += max(triangle[height-1][i], triangle[height-1][i+1])
        height -= 1
    
    return triangle[0][0]
