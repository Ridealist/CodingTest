list = [26, 7, 8, 42, 1, 2, 2, 5, 7, 8]

# 준보
def selection_sort(array: list):
    for i in range(len(array)):
        min_idx = i
        for j in range(i + 1, len(array)):
            if array[min_idx] > array[j]:
                min_idx = j
        array[i], array[min_idx] = array[min_idx], array[i]

    print(array)


# selection_sort(list)

# 회택
def sel_sort(target_li):
    idx = 0
    while idx < len(target_li):
        minVal = target_li[idx]
        minIdx = idx
        for i in range(idx, len(target_li)):
            if target_li[i] < minVal:
                minVal = target_li[i]
                minIdx = i
        target_li[minIdx], target_li[idx] = target_li[idx], target_li[minIdx]
        idx += 1
    return target_li


#####################################

list = [26, 7, 8, 42, 1, 2, 2, 5, 7, 8]
# 준보
def insertion_sort(array: list):
    for i in range(1, len(array)):
        # range에서 첫번째와 마지막 값을 넣어보기
        # edge 케이스를 생각해보는 것!
        for j in range(i):
            if array[i - 1 - j] > array[i - j]:
                # 디버깅!!
                print(i - j, i - 1 - j)
                array[i - j], array[i - 1 - j] = array[i - 1 - j], array[i - j]
            else:
                # 디버깅!!
                print(array)
                break

    print(array)


# 이코테 교재
def insertion_sort_book(array: list):
    for i in range(1, len(array)):
        for j in range(i, 0, -1):
            if array[j - 1] > array[j]:
                array[j - 1], array[j] = array[j], array[j - 1]
            else:
                break

    print(array)


insertion_sort(list)
# insertion_sort_book(list)
