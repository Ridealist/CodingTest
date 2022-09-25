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

for i in data[1:]:
    if result <= 1:
        result += int(i)
    else:
        if int(i) <= 1:
            result += int(i)
        else:
            result *= int(i)

## 여집합 구조!!
for i in data[1:]:
    num = int(i)
    if result <= 1 or num <= 1:
        result += num
    else:
        result *= num
