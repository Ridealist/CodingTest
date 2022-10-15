def find_next_index(l: list, i: int):
    cnt = 0
    if i == len(l) - 1:
        i = -1
    while l[i+1] == 0 and cnt <= len(l):
        i += 1
        cnt += 1
        if i == len(l)-1:
            i = -1
    if cnt > len(l):
        return -1
    return i+1

# print(find_next_index([0,0,0,0,0,0,0], 5))


def solution(food_times, k):
    i = 0
    for _ in range(k):
        food_times[i] -= 1
        i = find_next_index(food_times, i)
        if i == -1:
            return -1
    else:
        return i+1

print(solution([3, 1, 2], 5))


### 회택이 풀이

def solution(food_times, k):
    times = k // len(food_times)
    remainder = k % len(food_times) - 1
    extra = remainder + 1
    for i in range(len(food_times)):
        food_times[i] -= times
        if extra > 0:
            food_times[i] -= 1
            extra -= 1
            
    if sum(food_times) <= 0:
        return -1
    
    idx = (sum(filter(lambda x: x<0, food_times)) * -1 + remainder + 1) % len(food_times)
    print(food_times)
    print(sum(filter(lambda x: x<0, food_times)) * -1)
    print(remainder)
    print(times)
    
    return idx + 1