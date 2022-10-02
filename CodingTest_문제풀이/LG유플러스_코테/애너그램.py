def cutlist(arr):
    arr.sort(key=lambda x: len(x))
    
    res = []
    temp = []
    for i in range(len(arr)-1):
        if len(arr[i]) == len(arr[i+1]):
            temp.append(arr[i])
        else:
            temp.append(arr[i])
            res.append(temp)
            temp = []
    if temp:
        temp.append(arr[-1])
        res.append(temp)
    else:
        res.append([arr[-1]])
    return res


def count_anagram(l):
    res = []
    for i in l:
        if set(i) in res:
            continue
        else:
            res.append(str(i))
    return len(res)


def solution(arr):
    
    arr = list(map(str, arr))
    arr_list = cutlist(arr)
    answer = 0
    for l in arr_list:
        answer += count_anagram(l)
    
    return answer


##############################제출 정답

def solution(arr):
    
    res = []
    for i in arr:
        s = str(i)
        arr_dict = {}
        for j in s:
            if j in arr_dict:
                arr_dict[j] += 1
            else:
                arr_dict[j] = 1
        
        if arr_dict in res:
            continue
        else:
            res.append(arr_dict)
    return len(res)


# print(cutlist([123, 234, 213, 432, 234, 1234, 2341, 12345, 324]))