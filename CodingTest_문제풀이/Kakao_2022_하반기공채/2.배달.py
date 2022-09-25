def solution(cap, n, deliveries, pickups):
    result = 0
    start = n

    while start > 0:
        point = start-1
        for i in range(n-1, -1, -1):
            if deliveries[i]==0 and pickups[i]==0:
                continue
            else:
                point = i
                break
print(end)

        # print(point)
        s_deli = cap
        idx = point
        while idx > 0 and s_deli >= deliveries[idx]:
            s_deli -= deliveries[idx]
            deliveries[idx] = 0
            idx -= 1
        # idx는 delivereis

        s_pick = cap
        jdx = point
        while jdx > 0 and s_pick >= pickups[jdx]:
            s_pick -= pickups[jdx]
            pickups[jdx] = 0
            jdx -= 1
        # jdx는 pickups

        result += 2 * (point+1)
        n = max(idx, jdx)+1
    
    return result




deliveries = [1, 0, 3, 1, 2]

pickups = [0, 3, 0, 4, 0]

print(recursive(4, 5, deliveries, pickups))

"""
15
지금 재생 중
코딩테스트 Arrays
코드없는 프로그래밍
모든 재생목록 보기

5
지금 재생 중
코딩테스트 String
코드없는 프로그래밍
모든 재생목록 보기

10
지금 재생 중
코딩테스트 Sorting
코드없는 프로그래밍
모든 재생목록 보기

7
지금 재생 중
코딩테스트 Stack
코드없는 프로그래밍
모든 재생목록 보기

9
지금 재생 중
코딩테스트 HashMap
코드없는 프로그래밍
모든 재생목록 보기

14
지금 재생 중
코딩테스트 Dynamic Programming
코드없는 프로그래밍
모든 재생목록 보기

11
지금 재생 중
코딩테스트 BackTracking
코드없는 프로그래밍
모든 재생목록 보기
"""
