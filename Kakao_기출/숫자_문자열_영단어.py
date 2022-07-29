"""https://programmers.co.kr/learn/courses/30/lessons/81301#qna"""

num_list = [
    "zero",
    "one",
    "two",
    "three",
    "four",
    "five",
    "six",
    "seven",
    "eight",
    "nine",
]
for i, j in enumerate(num_list):
    s = str(i).join(s.split(j))


def solution(s):
    n = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    w = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    p = []
    for pair in zip(n, w):
        p.append(pair)

    answer = ""
    while len(s) > 0:
        for n, w in p:
            if s.startswith(n):
                answer = answer + n
                s = s.split(n)[-1]
                break
            elif s.startswith(w):
                answer = answer + n
                s = s.split(w)[-1]
                break
    answer = int(answer)
    return answer


def solution(s):
    answer = ""
    words = {
        "zero": "0",
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9",
    }
    word = ""
    for i in s:
        if i.isdigit():
            answer += i
            continue
        word += i
        if word in words:
            answer += words[word]
            word = ""
    return int(answer)
