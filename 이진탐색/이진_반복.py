def binary_search(array, target, start, end):
    result = None
    cnt = 0
    while start <= end:
        cnt += 1
        print(f"{cnt}번 반복. 시작:{start}, 끝:{end}")

        mid = (start + end) // 2
        # print(mid)
        # print(type(mid))
        if array[mid] == target:
            # print(array[mid], target)
            result = mid
            # print("결과: ", result)
            break
        elif array[mid] < target:
            start = mid + 1
        else:
            end = mid - 1
            
    # print(bool(result))
    # bool(0) = False 오류!!!
    if result is not None:
        print("찾으려는 위치:", result, "번째 인덱스")
    else:
        print("찾으려는 원소가 배열에 없습니다.")


array = [2*i for i in range(10)]

target = 6

start = 0
end = len(array) - 1

binary_search(array, target, start, end)