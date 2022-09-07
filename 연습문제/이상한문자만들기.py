"""
https://school.programmers.co.kr/learn/courses/30/lessons/12930?language=python3
"""

"""
list comprehension 구문의 if else 문은 평소 형식과 조금 다르다~!

예시 코드
>>> l = [22, 13, 45, 50, 98, 69, 43, 44, 1]
>>> [x+1 if x >= 45 else x+5 for x in l]
[27, 18, 46, 51, 99, 70, 48, 49, 6]

형식
[ 조건 만족 시 출력값 if 조건 else 조건 불만족 시 출력 값 for i in data] 
"""

# 제출 답
def makeupper(word):
    n_word = ""
    for i, val in enumerate(word):
        if i % 2 == 0:
            n_word += val.upper()
        else:
            n_word += val.lower()
    return n_word

def solution(s):
    s_list = s.split(" ")
    n_list = []
    for word in s_list:
       n_list.append(makeupper(word))
    return " ".join(n_list)


# 리팩토링 답
def makeupper(word):
    return "".join([word[i].upper() if i%2 == 0 else word[i].lower() for i in range(len(word))])

def solution(s):
    s_list = s.split(" ")
    for idx, word in enumerate(s_list):
        s_list[idx] = "".join([word[i].upper() if i%2 == 0 else word[i].lower() for i in range(len(word))])
    return " ".join(s_list)


# 한줄 풀이 답(다른사람 풀이 힌트)
def solution(s):
    return " ".join(map(lambda x: "".join([x[i].upper() if i%2 == 0 else x[i].lower() for i in range(len(x))]), s.split(" ")))