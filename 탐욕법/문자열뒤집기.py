"""
https://www.acmicpc.net/problem/1439
"""

# 백준 풀이 공부해보기!!!

from collections import deque

s = deque(map(int, input()))

# print(s)

d = {0:0, 1:0}

st = []
while s:
    poped = s.popleft()
    if not st:
        st.append(poped)
    else:
        if st[-1] == poped:
            st.append(poped)
        else:
            d[st[-1]] += 1
            st = [poped]

d[st[-1]] += 1

# print(d)

print(min(d[0], d[1]))


## 교재 풀이 공부
data = input()
count0 = 0 ##전부 0으로 바꾸는 경우
count1 = 0 ##전부 1로 바꾸는 경우

# 첫번째 원소 처리
if data[0] == "1":
    count0 += 1
else:
    count1 += 1

# 두번째 원소부터 모든 원소 확인
for i in range(len(data)-1):
    if data[i] == data[i+1]:
        pass
    # 다음 수에서 바뀐다면
    else:
        if data[i+1] == "0":
            count1 += 1
        else:
            count0 += 1


print(min(count0, count1))