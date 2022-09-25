"""
https://school.programmers.co.kr/learn/courses/30/lessons/42889
"""

# 준보 솔루션
def solution(N, stages):
    fail = []

    for i in range(1, N + 1):
        total = 0
        i_cnt = 0
        for stage in stages:
            if stage >= i:
                total += 1
            if stage == i:
                i_cnt += 1
        if total != 0:
            failure = i_cnt / total
        if total == 0:
            failure = 0
        fail.append((i, failure))

    l = sorted(fail, key=lambda f: f[1], reverse=True)

    answer = [i[0] for i in l]

    print(answer)
    return answer


# 회택 솔루션
def solution(N, stages: list):
    # li: list
    # for i in range(1, N+1):
    #     li.append(stage.count(i))

    li: list = [0] * (N + 1)
    for stage in stages:
        li[stage - 1] += 1

    failure = []
    for i in range(N):
        s = sum(li[i:])
        if s:
            fail = li[i] / s
        else:
            fail = 0
        failure.append((i + 1, fail))

    l = sorted(failure, key=lambda f: f[1], reverse=True)

    answer = [i[0] for i in l]

    print(answer)
    return answer


N = 4
stages = [4, 4, 4, 4, 4]

# N = 5
# stages = [2, 1, 2, 6, 2, 4, 3, 3]

solution(N, stages)
