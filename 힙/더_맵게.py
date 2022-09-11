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


# heapq 사용!!
# Wow!!!
import heapq

def solution(scoville, K):
    heapq.heapify(scoville)
    cnt = 0
    
    while len(scoville) > 1 and scoville[0] < K:
        m = heapq.heappop(scoville)
        sec_m = heapq.heappop(scoville)
        new = m + (sec_m * 2)
        heapq.heappush(scoville, new)
        cnt += 1
    
    if len(scoville) == 1:
        if heapq.heappop(scoville) >= K:
            return cnt
        return -1
    else:
        return cnt