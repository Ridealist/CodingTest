"""
변수를 적절히 설정하는 연습!

총 그룹수 result
현재 그룹 모험가수 group

for문 돌면서 group += 1 / 조건 만족하면 result += 1, group 초기화
"""

n = int(input())

fear = []
for i in map(int, input().split()):
    fear.append(i)

fear.sort()

idx = 0
M = 0
answer = 0
party = []
while idx < n:
    if fear[idx] > M:
        M = fear[idx]
    party.append(fear[idx])
    idx += 1
    # 이부분 고민!
    # if len(party) >= M: 크거나 같을 때로 해줘야 하는지??
    if len(party) == M:
        answer += 1
        print(party)
        party = []
        

print(answer)


## 교재 구현
result = 0 # 총 그룹수
count = 0 # 현재 그룹에 포함된 모험가 수

for i in fear:
    count += 1 # 현재 그룹에 모험가 추가
    if count >= i: # 현재 그룹에 포함된 모험가 수가 현재 공포도 이상이면, 그룹 결성
        result += 1 # 총 그룹 수 증가
        count = 0 # 현재 그룹 초기화

print(result)