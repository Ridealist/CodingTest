"""https://programmers.co.kr/learn/courses/30/lessons/42748"""


def solution1(array, commands):
    answer = []
    for com in commands:
        first = int(com[0])
        second = int(com[1])
        third = int(com[2])
        num = sorted(array[first - 1 : second])[third - 1]
        answer.append(num)
    return answer


def solution2(array, commands):
    answer = []
    for i, j, k in commands:
        answer.append(sorted(array[i - 1 : j])[k - 1])
    print(answer)
    return answer


def solution3(array, commands):
    answer = list(map(lambda x: sorted(array[x[0] - 1 : x[1]])[x[2] - 1], commands))
    print(answer)
    return answer


array = [1, 5, 2, 6, 3, 7, 4]
commands = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]
answer = [5, 6, 3]

solution2(array, commands)
