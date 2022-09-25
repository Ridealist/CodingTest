"""
https://school.programmers.co.kr/learn/courses/30/lessons/60058?language=python3
"""

## 문제 구조 이해!
## 항상 함수 분리가 좋은 것은 아니다.

"""
문제의 전체적인 흐름을 먼저 이해하자!

앞에서 부터 하나씩 함수로 만들며 처리하는게 좋을 수도 있지만
전체적인 그림을 그리고 푸는게 더 좋을 때도 많다.

u,v 나누기 -> 올바른 괄호 체크하기 -> 재귀

(올바른 괄호 체크 + 제귀)가 사실 하나의 과정임!

"""

def makeuv(p:str):
    if not p:
        return ""
    p_list = list(p)
    u = []
    while p_list:
        poped = p_list.pop(0)
        u.append(poped)
        if u.count("(") == u.count(")"):
            break
    v = p_list
    return "".join(u), "".join(v)


def solution(p:str):
    if not p:
        return ""
    u, v = makeuv(p)
    if u[0] == "(":
        return u + solution(v)
    temp = "(" + solution(v) + ")"
    u_list = list(u)
    u_list.pop(0)
    u_list.pop(len(u_list)-1)
    if not u_list:
        return temp
    for i in u_list:
        if i == "(":
            temp += ")"
        else:
            temp += "("
    return temp

print(makeuv("()))((()"))
print(solution("()))((()"))


### 약간의 Refactoring version.

def makeuv(p:str):
    p_list = list(p)
    u = []
    while p_list:
        poped = p_list.pop(0)
        u.append(poped)
        if u.count("(") == u.count(")"):
            break
    return "".join(u), "".join(p_list)


def solution(p:str):
    if not p:
        return ""
    u, v = makeuv(p)
    if u[0] == "(":
        return u + solution(v)
    temp = "(" + solution(v) + ")"
    u = u[1:len(u)-1]
    if not u:
        return temp
    for i in u:
        if i == ")":
            temp += "("
        else:
            temp += ")"
    return temp


### 다른분들 풀이 공부

## 문자열 분리하기 - count와 enumerate 이용하기
def makeuv(p:str):
    c = 0
    for idx, v in enumerate(p):
        if v == "(":
            c += 1
        if v == ")":
            c -= 1

        if c == 0:
            return p[:idx+1], p[idx+1:]


## 올바른 문자열 판별법
def isright(p:str):
    cnt = 0
    res = True
    for i in p:
        if i == "(":
            cnt += 1
        elif i == ")":
            cnt -= 1
        if cnt < 0:
            res = False
    return res

p = "()))((()"

print(isright(p))


## 올바른 문자열 판별법 - 스택활용(회택 아이디어)
def is_correct(p):
    st = []
    
    for i in p:
        if i == "(":
            st.append(i)
        elif i == ")":
            if st and st[-1] == "(":
                st.pop()
            else:
                st.append(i)
    if st:
        return False
    else:
        return True

# 문자열 바꾸기
p = "()))((()"
print("".join(list(map(lambda x:'(' if x==')' else ')', p[1:-1]))))