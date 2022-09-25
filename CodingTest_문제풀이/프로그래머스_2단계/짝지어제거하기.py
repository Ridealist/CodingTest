"""
https://school.programmers.co.kr/learn/courses/30/lessons/12973?language=python3
"""

def solution(s):
    st = []
    for w in s:
        if st and st[-1] == w:
            # print("제거: ", w)
            st.pop()
            # print(st)
        else:
            st.append(w)
            # print("추가: ", w)
            # print(st)
    if st:
        return 0
    else:
        return 1
    
    # return not(st) 
    # bool 자료형 리턴하도록 하는 방법!

