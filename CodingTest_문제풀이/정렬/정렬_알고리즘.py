def bubble_sort(array):
    n = len(array)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
    print(array)


# bubble_sort(array)

# 배열과 관계없이 전체 비교 -> 시간복잡도 O(n^2)
# 단 하나의 배열에서 진행 -> 공간복잡도 O(n)


def selection_sort(array):
    n = len(array)
    for i in range(n - 1):
        tmp = i
        for j in range(i + 1, n):
            if array[tmp] > array[j]:
                tmp = j
        array[i], array[tmp] = array[tmp], array[i]
    return array


def insertion_sort(array):
    n = len(array)
    for i in range(1, n):
        cur = i
        cur_array = array[i]
        for j in range(i - 1, -1, -1):
            if array[i] < array[j]:
                array[j + 1] = array[j]
                cur = j
        array[cur] = cur_array
    return array


array = [8, 4, 6, 2, 9, 1, 3, 7, 5]
print("before sort:", array)
print("after sort:", insertion_sort(array))
