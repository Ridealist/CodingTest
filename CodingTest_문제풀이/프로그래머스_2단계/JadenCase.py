"""
https://school.programmers.co.kr/learn/courses/30/lessons/12951
"""

"""
# issue_1
index error 대비

""[0] 빈스트링에 인덱스를 부과하면 error가 나지만
""[0:1] 슬라이싱은 에러 나지 않음

# issue_2
string.title()
 -> 처음 만나는 영문자를 대문자로
string.capitalize()
 -> 종류 무관 맨 처음 문자를 대문자로

# issue_3
s[i:j] / slice of s from i to j

s[i:j:k] / slice of s from i to j with step k

"""


def solution(s):
    return " ".join([i[0].upper() + i[1:] if len(i) >= 1 else '' for i in s.lower().split(" ")])

def solution(s):
    return " ".join([i[0:1].upper() + i[1:] for i in s.lower().split(" ")])

def solution(s):
    return " ".join([i.capitalize() for i in s.lower().split(" ")])

## 출제 의도에 맞는 풀이!
## 시간복잡도 및 공간복잡도 만족
## O(n), str 변수 하나 활용
def solution(s):
    answer = ''
    # 변수명 설정의 중요성!
    first_alph = True
    for c in s:
        if c == " ":
            answer += c
            first_alph = True
        else:
            if first_alph:
                answer += c.upper()
                first_alph = False
            else:
                answer += c.lower()
    return answer


"""
is_blank -> 좋지 않은 변수!
첫번째 글자인지 아닌지를 또 설정해줘야함.
"""
# def solution(s):
#     answer = ''
#     # 변수명 설정의 중요성!
#     isblank = False
#     for c in s:
#         if c == " ":
#             isblank = True
#         else:
#             isblank = False

#         if not isblank:
#             answer += c.upper()
#             answer += c
#             first_alph = True

#         else:
#             answer += c

#         else:
#             if first_alph:
#                 answer += c.upper()
#                 first_alph = False
#             else:
#                 answer += c.lower()
#     return answer