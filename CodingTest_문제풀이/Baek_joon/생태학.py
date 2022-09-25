"""
https://www.acmicpc.net/problem/4358
"""



"""
참조: https://daebaq27.tistory.com/57
백준에서 입력받는 방법

##1 for loop + input() 활용
-> 몇 개의 입력이 들어올지 첫줄에 있을 때
# 첫줄만 우선 입력 받음
n,m = map(int, input().split())
# 데이터 형식 지정
arr = []
# for loop
for _ in range(m):
    arr.append(list(map(int, input().split())))


##2 표준 입력을 파일로 설정
import sys
# 표준입력을 파일로 설정
sys.stdin = open("input_2924.txt", "r")
# input() 사용자 입력 받지 않고, 표준입력에 정의된 파일 읽음
n,m = map(int, input().split())
# list comprehension을 이용해 이후 입력값 받음
arr = [list(map(int, input().split())) for _ in range(m)]


##3 sys.stdin.readline() 활용
n,m = map(int, sys.stdin.readline().split())
(동일)

"""

import sys

trees = {}
tree_n = 0

sys.stdin = open("C:/Users/Junbo Koh/Desktop/CodingTest/Baek_joon/백준 예제 입력값/4358_input.txt", "rt")

for line in sys.stdin:
    if line == "\n":
        break
    line = line[:-1]
    tree = line.rstrip()
    tree_n += 1
    if tree in trees:
        trees[tree] += 1
    else:
        trees[tree] = 1

# sorted_tree = sorted(trees.items(), key=lambda x:x[0])

# print(sorted(trees.keys()))

for key in sorted(trees.keys()):
    percentage = round((trees[key]/tree_n)*100, 4)
    print(key, percentage)


# tree_list = []

# n, m = map(int, input().split())  # 앞의 글자는 n, 뒤의 글자는 m으로 할당됨.
# print(n, m)

# for _ in range()

# tree = map(str, input(data))

# print(tree)

# trees = {
#     "pine": 2,
#     "maple": 3,
#     "grass": 5,
# }


# sorted_trees = sorted(trees.items(), key=lambda x: x[0])
# for tree in sorted(trees.keys()):
#     print(tree, trees[tree])
# # print(sorted_trees)
