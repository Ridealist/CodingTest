"""
https://school.programmers.co.kr/learn/courses/30/lessons/12939
"""
### 다른 사람 풀이 공부
### return 값을 최대한 간단히 생각하기!!! 유연한 사고...
"""
2개의 숫자만 return 하는 것으로 str + 연산을 사용하는게 유리
or f-Stings 을 활용하기!
"""

def solution(s):
    s_list = list(map(int, s.split(" ")))
    # return str(min(s_list)) + " " + str(max(s_list))
    return f"{min(s_list)} {max(s_list)}"


## why?/??
"""
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: sequence item 0: expected str instance, int found

말그래도 " ".join([]) 리스트 안의 요소들은 str type이어야 join이 가능하다...
"""
def solution(s):
    s_list = list(map(int, s.split(" ")))
    # return " ".join([str(min(s_list)), str(max(s_list))])
    return " ".join(list(map(str, [min(s_list), max(s_list)])))


def solution(s):
    s_list = list(map(int, s.split(" ")))
    return " ".join([str(min(s_list)), str(max(s_list))])


## 처음 풀이
def solution(s):
    s_list = [int(i) for i in s.split(" ")]
    m = str(min(s_list))
    M = str(max(s_list))
    return " ".join([m, M])