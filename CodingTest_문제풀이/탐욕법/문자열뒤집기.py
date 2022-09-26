"""
https://www.acmicpc.net/problem/1439
"""

from collections import deque

s = deque(map(int, input()))

# print(s)

st = [0, 0]

d = {0:1, 1:0}

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

print(min(d[0], d[1]))


### 회택 풀이!!
S = "01110110110101001100"

## 000111000111
## 0101
### 똑같게 취급하도록!

zero_num = 0
one_num = 0

flag = None
for i in S:
    if i == "0" and flag != 0:
        flag = 0
        zero_num += 1
    elif i == "1" and flag != 1:
        flag = 1
        one_num += 1

print(min(zero_num, one_num))


### 교재 풀이 공부
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


### 백준 풀이 - 1
change = 0
prev = '?'
string = input()
for i in string:
    if i != prev: change += 1
    prev = i
print(change//2)


### 
data.count("01")
data.count("10")


### 백준 풀이 - 1
n = input()

print(len([x for x in n.split(n[0]) if x]))


## 백준 풀이 - 2
from itertools import*

print(list(*groupby(input())))

print(len([*groupby(input())])//2)
