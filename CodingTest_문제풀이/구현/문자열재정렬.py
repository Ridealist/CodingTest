"""
Edge Case
숫자의 합이 0인 경우

if num != 0:
    += str(num)
"""


data = input()

from string import ascii_uppercase

dic = {}
for i in ascii_uppercase:
    dic[i] = 0

# print(dic)

num = 0
for i in data:
    # print(i)
    if i.isalpha():
        dic[i] += 1
    else:
        num += int(i)

answer = str()
for key in dic.keys():
    answer += key * dic[key]

if num != 0:
    print(answer + str(num))
else:
    print(answer)