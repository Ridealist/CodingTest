

def binary_search(array, target, start, end):
    global cnt
    cnt += 1
    print(cnt, "번째 재귀함수 실행")
    n = len(array)
    middle = (start + end)//2
    if array[middle] > target:
        binary_search(array, target, start, middle)
    elif array[middle] < target:
        binary_search(array, target, middle, end)
    else:
        print("찾으려는 위치: ", middle)

cnt = 0

array = [2*i for i in range(10)]

target = 16

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