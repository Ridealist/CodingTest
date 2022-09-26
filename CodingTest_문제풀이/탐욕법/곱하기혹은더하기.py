l = list(map(int, input()))

# print(l)

answer = 0
for n in l:
    if n == 0:
        pass
    elif n == 1:
        answer += 1
    else:
        if answer == 0 or answer == 1:
            answer += n
        else:
            answer *= n

print(answer)


### 교재 풀이 공부
# 두 수 중에 하나라도 1이하인 경우는 더하기, 두 수 모두 2이상이면 곱하기

data = input()

result = int(data[0])

## 변수마다 조건의 분기
for i in data[1:]:
    if result <= 1:
        result += int(i)
    else:
        if int(i) <= 1:
            result += int(i)
        else:
            result *= int(i)

"""
## or/and 연산자는 "lazy"하게 계산 됨
## 참인 확률이 높은 것을 or 앞쪽에
## 거짓인 확률이 높은 것을 and 앞쪽에

## 좋지 않은 구조!

for i in l:
    if i==1 or i==0 or res==0 or res==1:
        res += i
    else:
        res *= i

print(res)
"""

## 여집합 구조!!
for i in data[1:]:
    num = int(i)
    if result <= 1 or num <= 1:
        result += num
    else:
        result *= num
