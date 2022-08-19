def solution(queue1, queue2):

    q, r = divmod(sum(queue1 + queue2), 2)
    if r != 0:
        return -1

    target = q

    sq1 = sum(queue1)
    sq2 = sum(queue2)

    if sq1 == sq2:
        return 0

    else:
        max_q = max(sq1, sq2)

        if sum(queue1) == max_q:
            max_queue = queue1
            min_queue = queue2
        else:
            max_queue = queue2
            min_queue = queue1

        cnt = 0
        while sum(max_queue) > target:
            p = max_queue.pop(0)
            min_queue.append(p)
            cnt += 1

        if sum(max_queue) == target:
            return cnt

        elif sum(max_queue) < target:
            while sum(min_queue) > target:
                p = min_queue.pop(0)
                max_queue.append(p)
                cnt += 1

            if sum(queue2) == target:
                return cnt

            else:
                return -1

        else:
            return -1


# 참고 코드
"""
import collections
import copy

def solution(queue1, queue2):
    a1 = collections.deque(queue1)
    a2 = collections.deque(queue2)
    
    answer = 0
    
    tmp = copy.deepcopy(a1)
    sum_1 = sum(a1)
    sum_2 = sum(a2)
    
    while True:
        if sum_1 > sum_2:
            popped = a1.popleft()
            a2.append(popped)
            sum_1 -= popped
            sum_2 += popped
        elif sum_2 > sum_1:
            popped = a2.popleft()
            a1.append(popped)
            sum_2 -= popped
            sum_1 += popped
        else:
            return answer
        answer += 1
        if tmp == a1:
            return -1
        if answer > len(queue1) + len(queue2) + 10:
            return -1
    return answer

"""
