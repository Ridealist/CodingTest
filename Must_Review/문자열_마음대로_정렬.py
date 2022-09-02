"""
https://school.programmers.co.kr/learn/courses/30/lessons/12915?language=python3
"""

"""
ASCII / Unicode
https://whatisthenext.tistory.com/103

# ord() -> 문자의 unicode 숫자를 return
# chr() -> unicode 숫자를 해당 문자로 변환
"""


def solution(strings, n):
    return sorted(sorted(strings), key=lambda x:x[n])


# strings = ["sun", "bed", "car"]
# for i in strings:
#     ord(i[0])

# a,b,c = map(int, input().split())

# l = [a,b,c]

def dictionary_sort(array: list):
    for word in array:
        word = word.lower()
        
    for i in range(n):
        for j in range(n-1-i):
            if array[j] > array[j+1]:
                array[j+1], array[j] = array[j], array[j+1]
    return array


# print(a)

#sort(l)
# print(l)