"""
https://school.programmers.co.kr/learn/courses/30/lessons/12926?language=python3
"""

"""
import string

string.ascii_lowercase
>>> string.ascii_lowercase
'abcdefghijklmnopqrstuvwxyz'

string.ascii_uppercase
>>> string.ascii_uppercase
'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
"""



def solution(s, n):
    list_s = list(s)
    lower = {i for i in range(97, 123)}
    upper = {i for i in range(65, 91)}
    
    result = []
    for alpha in list_s:
        if ord(alpha) in lower:
            new_ord = ord(alpha) + n
            if new_ord > 122:
                new_ord = 97 + (new_ord - 123)
            result.append(chr(new_ord))
        elif ord(alpha) in upper:
            new_ord = ord(alpha) + n
            if new_ord > 90:
                new_ord = 65 + (new_ord - 91)
            result.append(chr(new_ord))
        else:
            result.append(" ")
            
    return "".join(result)


def solution(s, n):
    lower_set = {i for i in range(ord("a"), ord("z")+1)}
    upper_set = {i for i in range(ord("A"), ord("Z")+1)}
    
    lower_list = [chr(i) for i in lower_set]*2
    upper_list = [chr(i) for i in upper_set]*2
    
    list_s = list(s)
    
    result = ""
    for i in list_s:
        if i in lower_list:
            result += lower_list[lower_list.index(i) + n]
        elif i in upper_list:
            result += upper_list[upper_list.index(i) + n]
        else:
            result += " "
    
    return result


def solution(s, n):
    list_s = list(s)
    
    answer = ""
    for i in list_s:
        if i.isupper():
            new_ord = (ord(i) - ord("A") + n) % 26 + ord("A")
            answer += chr(new_ord)
        elif i.islower():
            new_ord = (ord(i) - ord("a") + n) % 26 + ord("a")
            answer += chr(new_ord)
        else:
            answer += " "
    
    return answer