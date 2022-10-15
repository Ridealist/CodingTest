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


########### 회택 풀이

def rearrange(S):
    string = []
    sum_num = 0
    for i in S:
        if i.isalpha():
            string.append(i)
        elif i.isdigit():
            sum_num += int(i)
    string.sort(key=lambda x: ord(x))
    return "".join(string) + str(sum_num)
import bisect

def rearrange2(S):
    string = []
    sum_num = 0
    for i in S:
        if 65 <= ord(i) and 122 >= ord(i):
            bisect.insort_left(string, i, key= lambda x: ord(x))
        elif 48 <= ord(i) and 57 >= ord(i):
            sum_num += int(i)
    return "".join(string) + str(sum_num)