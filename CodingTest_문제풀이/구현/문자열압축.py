"""
https://school.programmers.co.kr/learn/courses/30/lessons/60057
"""


def cutstr(s):
    cuts = []
    for i in range(1, len(s)//2 + 1):
        cut = []
        for j in range(0, len(s), i):
            cut.append(s[j:j+i])
        cuts.append(cut)
    return cuts


# print(cutstr("ababcdcdababcdcd"))
def compress(cut: list):
    cnt = 1
    res = str()
    for i in range(len(cut)-1):
        if cut[i] == cut[i+1]:
            cnt += 1
        if cut[i] != cut[i+1] or i == (len(cut) - 2):
            if cnt == 1:
                res += cut[i]
            else:
                res += (str(cnt) + cut[i])
            cnt = 1
    
    return len(res)

print(compress(['aba', 'bcd', 'cda', 'bab', 'cdc', 'd']))

def solution(s):
    cuts = cutstr(s)
    m = 100000
    for cut in cuts:
        n = compress(cut)
        if m > n:
            m = n
    return m