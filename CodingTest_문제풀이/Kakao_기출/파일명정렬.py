"""
https://school.programmers.co.kr/learn/courses/30/lessons/17686
"""

def splitpart(word: str):
    head = ""
    number = ""
    tail = ""
    # npointer = False
    num_end = False
    for c in word:
        if not c.isdigit() and not num_start:
            head += c
        if c.isdigit():
            num_start = True
            number += c
        
        if c.isdigit():
            npointer = True
        else:
            npointer = False
        if head and number and not npointer:
            break
            
        if not npointer:
            head += c
        if npointer:
            number += c

    return head, number


## 리팩토링
def splitpart(word: str):
    head = ""
    number = ""
    num_start = False
    for c in word:
        if not c.isdigit() and num_start:
            break

        if not c.isdigit():
            head += c
        if c.isdigit():
            num_start = True
            number += c

    return head.lower(), int(number)

def solution(files: list):
    return sorted(files, key = lambda x: (splitpart(x)[0], splitpart(x)[1]))


## 회택 풀이

def solution(files: list):
    indices = []
    for i, file in enumerate(files):
        flag = 0
        head = ""
        num = ""
        for c in file:
            if c.isdigit():
                flag = 1
            if flag == 1 and not c.isdigit():
                break
            
            if flag == 0:
                head += c
            if flag == 1:
                num += c

        data = {"idx": i, "head": head.lower(), "num": int(num)}
        indices.append(data)
    
    s_indices = sorted(indices, key=lambda x: (x["head"], x["num"]))
    
    return [files[i["idx"]] for i in s_indices]