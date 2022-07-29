"""https://programmers.co.kr/learn/courses/30/lessons/42577?language=python3"""


def solution(phone_book):
    # answer = True
    for i in range(len(phone_book)):
        for n in range(1, len(phone_book) - i):
            if len(phone_book[i]) >= len(phone_book[i + n]):
                if phone_book[i][0 : len(phone_book[i + n])] == phone_book[i + n]:
                    # answer = False
                    return False
            else:
                if phone_book[i] == phone_book[i + n][0 : len(phone_book[i])]:
                    # answer = False
                    return False
    return True


def solution(phone_book):
    phone_book = sorted(phone_book)
    for i in range(len(phone_book)):
        for j in range(i + 1, len(phone_book)):
            if phone_book[i][0] == phone_book[j][0]:
                if phone_book[j].startswith(phone_book[i]):
                    return False
            # if phone_book[i].startswith(phone_book[j]):
            #     return False
    return True


def solution(phone_book):
    s = set(phone_book)

    for phone_number in phone_book:
        for i in range(1, len(phone_number)):
            if phone_number[0:i] in s:
                return False
    return True


testcaseArr = [
    [["119", "97674223", "1195524421"], False],
    [["123", "456", "789"], True],
    [["12", "123", "1235", "567", "88"], False],
]

for row in testcaseArr:
    result = solution(row[0])
    print(result == row[1])
