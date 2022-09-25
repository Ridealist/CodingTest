# n, target = map(int, input().split())
# array = list(map(int, input().split()))

# array.sort(reverse=True)

# idx = 1
# total = 0
# while total < target:
#     idx += 1
#     total = 0
#     for length in array[:idx]:
#         total += length - array[idx]

# print(array[idx])

#######################
# n, target = map(int, input().split())
# array = list(map(int, input().split()))

# array.sort()


def search_height(array, target, start, end):
    array.sort()
    mid = (start + end) // 2
    total = sum([i-array[mid] for i in array[mid+1:]])
    while total < target:
        if total > target:
            print(total, target)
            start = mid + 1
        elif total < target:
            print(total, target)
            end = mid - 1
    return mid

n = 4
target = 6
array = [19, 15, 10, 17]


##############################

n, target = map(int, input().split())
array = list(map(int, input().split()))

start = 0
end = max(array)

result = 0
while start <= end:
    total = 0
    mid = (start + end) // 2
    # sort 시간 단축 필요! 굳이 필요 없음
    # total = sum([i-mid for i in array if i > mid])
    for x in array:
        if x > mid:
            total += x - mid

    if total > target:
        result = mid
        start = mid + 1

    elif total < target:
        end = mid - 1

    # 논리적으로 완결하지 않으면 실행 안됨!
    # 같은 경우 처리도 해줘야.
    else:
        result = mid
        break

print(result)

