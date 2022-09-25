# 공 개수 n / 공 최대 무게 m
n, m = map(int, input().split())

boal = list(map(int, input().split()))

dic_boal = {i:0 for i in range(1, m+1)}

# print(dic_boal)

for i in boal:
    dic_boal[i] += 1

answer = 0
sub = 0
for i in range(1, m+1):
    sub += dic_boal[i]
    answer += dic_boal[i] * (n - sub)

print(answer)