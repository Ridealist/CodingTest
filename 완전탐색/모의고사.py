"""https://programmers.co.kr/learn/courses/30/lessons/42840?language=python"""


def solution(answers):
    first = []
    second = []
    third = []
    for i in range(len(answers)):
        first.append(i % 5 + 1)
        if i % 2 == 0:
            second.append(2)
        elif i % 2 == 1:
            if i % 8 == 5:
                second.append(4)
            elif i % 8 == 7:
                second.append(5)
            else:
                second.append(i % 8)
        if (i % 10) // 2 == 0:
            third.append(3)
        elif (i % 10) // 2 == 1:
            third.append(1)
        elif (i % 10) // 2 == 2:
            third.append(2)
        elif (i % 10) // 2 == 3:
            third.append(4)
        elif (i % 10) // 2 == 4:
            third.append(5)

    f_cnt = 0
    s_cnt = 0
    t_cnt = 0
    for i in range(len(answers)):
        if answers[i] == first[i]:
            f_cnt += 1
        if answers[i] == second[i]:
            s_cnt += 1
        if answers[i] == third[i]:
            t_cnt += 1

    maximum = max([f_cnt, s_cnt, t_cnt])

    answer = []
    if maximum == f_cnt:
        answer.append(1)
    if maximum == s_cnt:
        answer.append(2)
    if maximum == t_cnt:
        answer.append(3)

    answer = sorted(answer)
    return answer


def solution2(answers):
    pattern1 = [1, 2, 3, 4, 5]
    pattern2 = [2, 1, 2, 3, 2, 4, 2, 5]
    pattern3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    scores = [0, 0, 0]

    for idx, answer in enumerate(answers):
        if answer == pattern1[idx % len(pattern1)]:
            scores[0] += 1
        if answer == pattern2[idx % len(pattern2)]:
            scores[1] += 1
        if answer == pattern3[idx % len(pattern3)]:
            scores[2] += 1

    # print(score)
    answer = []
    for idx, score in enumerate(scores):
        if score == max(scores):
            answer.append(idx + 1)

    print(answer)
    return answer


from itertools import cycle


def solution3(answers):
    giveups = [
        cycle([1, 2, 3, 4, 5]),
        cycle([2, 1, 2, 3, 2, 4, 2, 5]),
        cycle([3, 3, 1, 1, 2, 2, 4, 4, 5, 5]),
    ]
    scores = [0, 0, 0]

    for i in range(len(giveups)):
        for a in answers:
            if a == next(giveups[i]):
                scores[i] += 1

    print(scores)

    highest = max(scores)
    answer = [idx + 1 for idx, score in enumerate(scores) if score == highest]
    print(answer)
    return answer


# answers	return
# [1,2,3,4,5]	[1]
# [1,3,2,4,2]	[1,2,3]

answers1 = [1, 2, 3, 4, 5]
answers2 = [1, 3, 2, 4, 2]

solution3(answers1)
