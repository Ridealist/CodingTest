"""
이코테 110-111p
"""


def solution(n, directions):
    cur_pos = [1, 1]
    for dir in directions:
        if dir == "R":
            if cur_pos[1] == n:
                continue
            else:
                cur_pos[1] += 1
        if dir == "L":
            if cur_pos[1] == 1:
                continue
            else:
                cur_pos[1] -= 1
        if dir == "U":
            if cur_pos[0] == 1:
                continue
            else:
                cur_pos[0] -= 1
        if dir == "D":
            if cur_pos[0] == n:
                continue
            else:
                cur_pos[0] += 1
    print(cur_pos)
    return cur_pos


def solution(n, directions):
    direct = ["R", "L", "U", "D"]
    row = [0, 0, -1, 1]
    col = [1, -1, 0, 0]

    cur_pos = [1, 1]
    for direction in directions:
        for idx, dir in enumerate(direct):
            if direction == dir:
                if cur_pos[0] == 1 & direction == "L":
                    continue
                elif cur_pos[0] == n & direction == "R":
                    continue
                else:
                    cur_pos[0] += row[idx]

                if cur_pos[1] == 1 & direction == "U":
                    continue
                elif cur_pos[1] == n & direction == "D":
                    continue
                else:
                    cur_pos[1] += col[idx]
    print(cur_pos)
    return cur_pos


n = 5
directions = ["R", "R", "R", "U", "D", "D"]

solution(n, directions)
