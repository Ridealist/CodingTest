"""
https://school.programmers.co.kr/learn/courses/30/lessons/60057
"""

"""

제한 범위 설정하기 연습
가능한 범위를 항상 생각하기!

가능한 문자열의 최대 길이는 압축되지 않는 것!

m = len(s)

"""


def cutstr(s):
    cuts = []
    for i in range(1, len(s) // 2 + 1):
        cut = []
        for j in range(0, len(s), i):
            cut.append(s[j:j+i])
        cuts.append(cut)
    return cuts


print(cutstr("xababcdcdababcdcd"))
def compress(cut: list):
    cnt = 1
    res = str()
    for i in range(len(cut)-1):
        if cut[i] == cut[i+1]:
            cnt += 1
        if cut[i] != cut[i+1]:
            if cnt == 1:
                res += cut[i]
            else:
                res += (str(cnt) + cut[i])
            cnt = 1
    if cut[-1] == cut[-2]:
        if cnt == 1:
            res += cut[-1]
        else:
            res += (str(cnt) + cut[i])
    
    return res
    return len(res)

print(compress(['ab', 'ab', 'cd', 'cd', 'ab', 'ab', 'cd', 'cd']))

def solution(s):
    cuts = cutstr(s)    
    ## 제한 범위 설정하기 연습
    ## 가능한 범위를 항상 생각하기!
    m = len(s)
    for cut in cuts:
        n = compress(cut)
        if m > n:
            m = n
    return m



### 교재 풀이 공부
def solution(s):
    answer = len(s)

    # 1개 단위부터 압축 단위를 늘려가며 확인
    for step in range(1, len(s)//2 + 1):
        compressed = ""
        prev = s[0:step] # 앞에서부터 step만큼의 문자열 추출
        cnt = 1
        for j in range(step, len(s), step):
            if prev == s[j:j + step]:
                cnt += 1
            else:
                compressed += str(cnt) + prev if cnt >= 2 else prev
                prev = s[j:j + step] # 상태 초기화
                cnt = 1
        # 남아 있는 문자열에 대해 처리
        compressed += str(cnt) + prev if cnt >= 2 else prev
        n = len(compressed)
        if answer > n:
            answer = n
    
    return answer

