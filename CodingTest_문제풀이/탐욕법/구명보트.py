"""
https://school.programmers.co.kr/learn/courses/30/lessons/42885
"""


# 정확성은 통과 효율성 실패
def solution(people, limit):
    visited = [False]*len(people)
    cnt = 0
    for i in range(len(people)):
        if visited[i] is True:
            continue
        visited[i] = True
        temp_max = 0
        m_idx = None
        for j in range(i+1, len(people)):
            if visited[j] is True:
                continue
            if people[j] > temp_max and limit-people[i] >= people[j]:
                temp_max = people[j]
                m_idx = j
        if m_idx:
            visited[m_idx] = True
        cnt += 1
    return cnt


# 두번째 도전 성공!!
from collections import deque

def solution(people, limit):
    people.sort()
    q = deque(people)
    
    cnt = 0
    while q:
        M = q.pop()
        if q and q[0] <= limit - M:
            q.popleft()
        cnt += 1
            
    return cnt


# 다른 사람 아이디어로 변용
def solution(people, limit):
    people.sort()
    
    cnt = 0
    start = 0
    end = len(people) - 1
    while start <= end:
        M = people[end]
        m = people[start]
        if m <= limit - M:
            start += 1
        end -= 1
        cnt += 1
    return cnt



## 다른 사람 풀이 공부
"""
# 인덱스만 비교하는 방법 굳!
# 인덱스를 변수로 만들고
# 조건에 따라 인덱스를 변경시키며 while문 돌리기

pop(0) 의 경우 데이터를 지우고 한칸씩 앞으로 당기기 때문에 O(1)이 아니라 O(n)이 됩니다. 
그래서 people을 collections.deque()로 만들어 popleft()를 사용하면 시간초과가 나지 않고 해결됩니다.
"""
def solution(people, limit) :
    answer = 0
    people.sort()

    a = 0
    b = len(people) - 1
    while a <= b :
        if people[b] + people[a] <= limit :
            a += 1
            #answer += 1
        b -= 1
        answer += 1
    return answer #len(people) - answer