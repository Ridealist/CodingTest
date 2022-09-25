def solution1(n):
    not_three = 0
    for i in range(n + 1):
        if "3" in str(i):
            continue
        else:
            not_three += 5 * 9 * 5 * 9

    total = 0
    for i in range(n + 1):
        total += 6 * 10 * 6 * 10

    answer = total - not_three

    print(answer)
    return answer


def solution2(n):
    not_three = 5 * 9 * 5 * 9
    total = 6 * 10 * 6 * 10
    three = total - not_three

    cnt = 0
    cnt_3 = 0
    for i in range(n + 1):
        if i == 3 or i == 13:
            cnt_3 += 1
        else:
            cnt += 1

    answer = cnt * three + cnt_3 * total
    print(answer)
    return answer


def solution(n):
    cnt = 0
    for hour in range(n + 1):
        for minute in range(60):
            for second in range(60):
                if str(3) in str(second) + str(minute) + str(hour):
                    cnt += 1
                else:
                    continue

    print(cnt)
    return cnt


solution1(5)
