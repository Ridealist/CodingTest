

def binary_search(array, target, start, end):
    global cnt
    cnt += 1
    print(cnt, "번째 재귀함수 실행")
    if start > end:
        return None
    middle = (start + end)//2
    if array[middle] > target:
        binary_search(array, target, start, middle - 1)
    elif array[middle] < target:
        binary_search(array, target, middle + 1, end)
    else:
        print("찾으려는 위치: ", middle, "번째 인덱스")

cnt = 0

array = [2*i for i in range(10)]

target = 15

start = 0
end = len(array) - 1

binary_search(array, target, start, end)

# middle_idx = (start_idx + end_idx)//2

# if a[middle_idx] < target:
#     start_ldx = middle_idx
# elif a[middle_idx] > target:
#     end_idx = middle_idx
# else:
#     print("찾으려는 위치: ", middle_idx)