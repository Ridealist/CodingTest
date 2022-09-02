"""https://programmers.co.kr/learn/courses/30/lessons/42746?language=python3"""


def solution1(numbers):
    for i in range(1, len(numbers)):
        for j in range(i):
            if int(str(numbers[i - 1 - j]) + str(numbers[i - j])) >= int(
                str(numbers[i - j]) + str(numbers[i - 1 - j])
            ):
                break
            if int(str(numbers[i - 1 - j]) + str(numbers[i - j])) < int(
                str(numbers[i - j]) + str(numbers[i - 1 - j])
            ):
                behind = numbers[i - j]
                front = numbers[i - 1 - j]
                numbers[i - 1 - j] = behind
                numbers[i - j] = front
    answer = ""
    for n in numbers:
        answer += str(n)
    print(answer)
    return answer


def makePermutation(int_numList):
    from itertools import permutations
    number_list = []
    for numset in permutations(int_numList, len(int_numList)):
        # print(numset)
        number = ""
        for i in range(len(numset)):
            number += str(numset[i])
        number_list.append(int(number))

    # print(number_list)
    return number_list


def solution2(numbers):
    number_list = makePermutation(numbers)
    answer = str(max(number_list))
    print(answer)
    return answer


def solution3(numbers):
    str_number = ""
    for i in range(9, 0, -1):
        for num in numbers:
            if num == i:
                str_number+=str(num)
            if str(num)[0] == i:
                






numbers1 = [6, 10, 2]
numbers2 = [3, 30, 34, 5, 9]


solution2(numbers2)

# numbers	return
# [6, 10, 2]	"6210"
# [3, 30, 34, 5, 9]	"9534330"
