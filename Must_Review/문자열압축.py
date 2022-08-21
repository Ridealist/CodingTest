"""
https://school.programmers.co.kr/learn/courses/30/lessons/60057?language=python3
"""

# 1st. 실패
# 2nd. 성공 / 50m 소요 (2022-08-21)


from re import T


def make_list(s, n):
    l = []
    while s and len(s) >= n:
        pop = s[:n]
        s = s[n:]
        l.append(pop)
    if len(s) < n and len(s) > 0:
        l.append(s)
    # print(l)
    if len(l) == 0:
        return s
    return l

def make_zip(l: list):
    result = ''
    cnt = 1
    temp = l[0]
    l = l[1:]
    if not l:
        return temp
    while l:
        poped = l.pop(0)
        if temp == poped:
            cnt += 1
        else:
            # 압축실행
            if cnt == 1:
                result += f"{temp}"
            else:
                result += f"{cnt}{temp}"
            # 초기화
            temp = poped
            cnt = 1
        if len(l) == 0:
            if cnt == 1:
                result += f"{temp}"
            else:
                result += f"{cnt}{temp}"

    # print(result)
    return result

def solution(s):
    answer = 1000
    for i in range(1, len(s)+1):
        l = make_list(s, i)
        result = make_zip(l)
        # int(len(result))
        if len(result) < answer:
            answer = len(result)

    return answer



## 프로그래머스 풀이 공부

def compress(s, tok_len):
    # tok_len의 step!! "range(stop) -> range object range(start, stop[, step]) -> range object"
    words = [s[i:i+tok_len] for i in range(0, len(s), tok_len)]
    
    res = []
    cur_word = words[0]
    cur_cnt = 1
    # zip 함수의 새로운 용법
    """
    zip(*iterables, strict=False) --> Yield tuples until an input is exhausted.
    >>> list(zip('abcdefg', range(3), range(4)))
    [('a', 0, 0), ('b', 1, 1), ('c', 2, 2)]
    """
    for pre, post in zip(words, words[1:] + [""]):
        if pre == post:
            cur_cnt += 1
        else:
            res.append([cur_word, cur_cnt])
            cur_word = post
            cur_cnt = 1
    return sum(len(word) + (len(str(cnt)) if cnt > 1 else 0) for word, cnt in res)

    # min 함수의 비용 문제
def solution(s):
    # min에 넣을 때 리스트를 안만들고 바로 comprehension을 쓰면 메모리 오류가 나지 않는군요
    return min(compress(s, tok_len) for tok_len in list(range(1, int(len(s)/2)+1)) + [len(s)])

def solution(s):
    answer = 1000
    ## 엣지 케이스 확인! -> +1 / +2의 차이
    for tok_len in range(1, int(len(s)/2)+2):
        temp = compress(s, tok_len)
        if temp < answer:
            answer = temp
    return answer


s = "aabbaccc"
tok_len = 2

words = [s[i:i+tok_len] for i in range(0, len(s), tok_len)]
print(words)

for i in zip(words, words[1:] + [""]):
    print(i)

