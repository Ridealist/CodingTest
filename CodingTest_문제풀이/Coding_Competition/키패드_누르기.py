"""
https://school.programmers.co.kr/learn/courses/30/lessons/67256#
"""

"""
1. 함수는 하나의 기능만 하도록!
   - 거리를 구하는 함수는 거리만! 구해야 함.
   - 함수가 여러값을 리턴하는건 좋은 구조가 아님
2. 가능한 모든 경우를 생각하기
   - 거리가 0인 경우도 존재! (이미 눌러있는 곳에 같은 키를 누르는 경우)
   - 전체 집합을 항상 생각하기
3. 2차원 배열을 고려하기!
   - 2차원 배열 기준에 익숙해지도록
4. 함수 이름을 깔끔하게
   - get_dist
   - find_pos 등등 명확한 의미
"""


def find_pos(val):
    keypads = [[1, 2, 3], [4, 5, 6], [7, 8, 9], ["*", 0, "#"]]
    for i, row in enumerate(keypads):
        for j, col in enumerate(row):
            if val == col:
                cor = (i, j)
                # print(cor)
                return cor


def get_dist(n, cur_hand):
    n_pos = find_pos(n)
    cur_hand_pos = find_pos(cur_hand)
    dist = abs(n_pos[0] - cur_hand_pos[0]) + abs(n_pos[1] - cur_hand_pos[1])
    return dist


def get_dist(n, cur_hand):
    d_dict = {0: 0, 1: 1, 2: 2, 3: 1, 4: 2, 5: 3, 6: 2, 7: 3, 8: 4, 9: 3, 10: 4}
    dist = d_dict[abs(n - cur_hand)]
    return dist


def get_dist(n, cur_hand):
    pad = {
        1: (0, 0),
        2: (0, 1),
        3: (0, 2),
        4: (1, 0),
        5: (1, 1),
        6: (1, 2),
        7: (2, 0),
        8: (2, 1),
        9: (2, 2),
        10: (3, 0),
        11: (3, 1),
        12: (3, 2),
    }
    dist = abs(pad[n][0] - pad[cur_hand][0]) + abs(pad[n][1] - pad[cur_hand][1])
    return dist


def solution(numbers, hand):
    answer = ""
    # new_numbers = []
    # for n in numbers:
    #     if n == 0:
    #         new_numbers.append(int(11))
    #     else:
    #         new_numbers.append(int(n))
    L = [1, 4, 7]
    R = [3, 6, 9]
    # curr_lh = 10
    # curr_rh = 12
    curr_lh = "*"
    curr_rh = "#"
    for n in numbers:
        if n in L:
            answer += "L"
            curr_lh = n
        elif n in R:
            answer += "R"
            curr_rh = n
        else:
            l_dist = get_dist(n, curr_lh)
            r_dist = get_dist(n, curr_rh)
            if l_dist < r_dist:
                answer += "L"
                curr_lh = n
            elif l_dist > r_dist:
                answer += "R"
                curr_rh = n
            else:
                if hand == "right":
                    answer += "R"
                    curr_rh = n
                else:
                    answer += "L"
                    curr_lh = n
    return answer
