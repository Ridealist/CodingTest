scoville = [1, 2, 3, 9, 10, 12]
K = 7


def solution(scoville, K):
    count = 0
    scoville = sorted(scoville)
    try:
        while int(scoville[0]) < int(K):
            new_sco = scoville[0] + (scoville[1] * 2)
            # scoville.remove(scoville[0])
            ## index=0 을 두번 삭제해야...
            # scoville.remove(scoville[1])
            del scoville[0:2]
            scoville.append(new_sco)
            scoville = sorted(scoville)
            count += 1
            # print(scoville)
            # print(count)
        return count
    except:
        return -1


result = solution(scoville, K)
print(result)
