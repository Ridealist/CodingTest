# import sys

# input_data = sys.stdin.readline().rstrip()

n = int(input())
n_array = list(map(int, input().split()))
# n_array.sort()

m = int(input())
m_array = list(map(int, input().split()))


def binary_search(array:list, target:int, start:int, end:int):
    if start > end:
        return False

    mid = (start+end) // 2
    if array[mid] == target:
        # print("비교값: ", array[mid], "목표값: ", target)
        return True
    elif array[mid] > target:
        # print("비교값: ", array[mid], "목표값: ", target)
        return binary_search(array, target, start, mid-1)
    elif array[mid] < target:
        # print("비교값: ", array[mid], "목표값: ", target)
        return binary_search(array, target, mid+1, end)


def binary_search(array:list, target:int, start:int, end:int):
    while start <= end:
        mid = (start + end)//2
        if array[mid] == target:
            return True
        elif array[mid] < target:
            start = mid + 1
        else:
            end = mid - 1
    return False






# print(binary_search([1,2,3,4,5], 7, 0, 4))


def search_part(n_list, m_list):
    n_list.sort()
    for i in m_list:
        if binary_search(n_list, i, 0, len(n_list)-1):
            print("yes", end=" ")
        else:
            print("no", end=" ")



n = 5
n_list = [8, 3, 7, 9, 2]

m = 3
m_list = [5, 7, 9]

search_part(n_list, m_list)