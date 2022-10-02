def devide(s: str):
    res = []
    flag = 0
    start = 0
    for i in range(len(s)):
        if s[i].isnumeric():
            continue
        
        if s[i] == "(":
            flag += 1
        if s[i] == ")":
            flag -= 1
        
        if flag == 0:
            res.append(s[start:i+1])
            start = i+1
    return res # list


def extend(s:str):
    if "(" not in s:
        return s
    if "(" in s:
        i = s.find("(")
        # j = s.rfind(")")
        # print(s[:i], s[i:])
        num = s[:i]
        dup = s[i+1:-1]
        temp = str()
        if "(" in dup:
            for i in devide(dup):
                temp += extend(i)
            return int(num) * temp
        else:
            temp += int(num) * dup
            return temp

# print(devide("2(3(hi)co)"))

print(extend("2(2(hi)2(co))"))


################################## 제출 정답!

def devide(s: str):
    res = []
    flag = 0
    start = 0
    for i in range(len(s)):
        if s[i].isnumeric():
            continue
        
        if s[i] == "(":
            flag += 1
        if s[i] == ")":
            flag -= 1
        
        if flag == 0:
            res.append(s[start:i+1])
            start = i+1
    return res # list

def extend(s:str):
    if "(" not in s:
        return s
    if "(" in s:
        i = s.find("(")
        # j = s.rfind(")")
        # print(s[:i], s[i:])
        num = s[:i]
        dup = s[i+1:-1]
        temp = str()
        if "(" in dup:
            for i in devide(dup):
                temp += extend(i)
            return int(num) * temp
        else:
            temp += int(num) * dup
            return temp

def solution(compressed):
    arr_list = devide(compressed)

    answer = str()
    for a in arr_list:
        answer += extend(a)

    return answer


#####################################

"""
1. 입력이 빈 문자열인 경우, 빈 문자열을 반환합니다. 
2. 문자열 w를 두 "균형잡힌 괄호 문자열" u, v로 분리합니다. 단, u는 "균형잡힌 괄호 문자열"로 더 이상 분리할 수 없어야 하며, v는 빈 문자열이 될 수 있습니다. 
3. 문자열 u가 "올바른 괄호 문자열" 이라면 문자열 v에 대해 1단계부터 다시 수행합니다. 
  3-1. 수행한 결과 문자열을 u에 이어 붙인 후 반환합니다. 
4. 문자열 u가 "올바른 괄호 문자열"이 아니라면 아래 과정을 수행합니다. 
  4-1. 빈 문자열에 첫 번째 문자로 '('를 붙입니다. 
  4-2. 문자열 v에 대해 1단계부터 재귀적으로 수행한 결과 문자열을 이어 붙입니다. 
  4-3. ')'를 다시 붙입니다. 
  4-4. u의 첫 번째와 마지막 문자를 제거하고, 나머지 문자열의 괄호 방향을 뒤집어서 뒤에 붙입니다. 
  4-5. 생성된 문자열을 반환합니다.
"""


def divide(s: str):
    flag = 0
    for i in range(len(s)):
        if s[i].isnumeric():
            continue
        
        if s[i] == "(":
            flag += 1
        elif s[i] == ")":
            flag -= 1
        
        if flag == 0:
            idx = i
            break
    return s[:idx+1], s[idx+1:]


def decompress(s: str):
    # 3. 문자열 u가 "해독해야 할 문자열"이 아니라면 v에 대해 1단계부터 다시 수행합니다. 
    # 3-1. 수행한 결과 문자열을 u에 이어 붙인 후 반환합니다. 
    if "(" not in s:
        return s
    # 4. 문자열 u가 "해독해야 할 문자열"이라면 아래 과정을 수행합니다. 
    else:
        start = s.find("(")
        end = s.rfind(")")
        # 4-1. 숫자 부분과 괄호 안 부분으로 나눕니다.
        num = int(s[:start])
        body = s[start+1:end]

    # 4-2. 괄호 안 부분에 다시 괄호가 있다면 문자열에 대해 1단계부터 다시 수행합니다.
    if "(" in body:
        u, v = divide(body)
        return num * (decompress(u) + decompress(v))
    # 4-3. 숫자 부분과 괄호 안 부분을 조합해 "해독완료 된 문자열"을 반환합니다.
    else:
        return num * body


def solution(compressed):
    # 1. 입력이 빈 문자열인 경우, 빈 문자열을 반환합니다. 
    # 재귀 종료 조건 명시!
    if not compressed:
        return ""
    # 2. 문자열 w를 두 "문자열 압축 유닛" u, v로 분리합니다.
    # 단, u는 "더 작은 유닛"으로 더 이상 분리할 수 없어야 하며, v는 빈 문자열이 될 수 있습니다. 
    u, v = divide(compressed)
    return decompress(u) + solution(v)

# print(decompress('2(3(hi)co)'))

print(solution("2(3(hi)co)"))
    