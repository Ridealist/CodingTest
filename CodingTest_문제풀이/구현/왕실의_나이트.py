"""
이코테 실전문제 115p
"""


def solution1(position):
    row = [str(i) for i in range(1, 9)]
    col = ["a", "b", "c", "d", "e", "f", "g", "h"]

    cur_col = position[0]
    cur_row = position[1]

    cur_row_idx = row.index(cur_row)
    cur_col_idx = col.index(cur_col)

    row_move1 = [2, 2, -2, -2]
    cor_move1 = [1, -1, 1, -1]

    cor_move2 = [2, 2, -2, -2]
    row_move2 = [1, -1, 1, -1]

    answer = 0
    for i in range(4):
        try:
            cur_row_idx += row_move1[i]
            row.index(cur_row_idx)
            cur_col_idx += cor_move1[i]
            col.index(cur_col_idx)
            answer += 1
        except:
            continue

    for i in range(4):
        try:
            cur_col_idx += cor_move2[i]
            col.index(cur_col_idx)
            cur_row_idx += row_move2[i]
            row.index(cur_row_idx)
            answer += 1
        except:
            continue

    print(answer)
    return answer


def solution2(position):
    col = {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5, "f": 6, "g": 7, "h": 8}

    col_num = col[position[0]]
    row_num = int(position[1])

    row_move1 = [2, 2, -2, -2]
    cor_move1 = [1, -1, 1, -1]

    cor_move2 = [2, 2, -2, -2]
    row_move2 = [1, -1, 1, -1]

    answer = 0
    for i in range(4):
        col_num = col[position[0]]
        row_num = int(position[1])
        row_num += row_move1[i]
        col_num += cor_move1[i]
        if row_num <= 0 or row_num >= 9 or col_num <= 0 or row_num >= 9:
            continue
        else:
            answer += 1

    for i in range(4):
        col_num = col[position[0]]
        row_num = int(position[1])
        col_num += cor_move2[i]
        row_num += row_move2[i]
        if row_num <= 0 or row_num >= 9 or col_num <= 0 or row_num >= 9:
            continue
        else:
            answer += 1

    print(answer)
    return answer


def solution(pos):
    row = int(pos[1])
    col = int(ord(pos[0])) - int(ord("a")) + 1

    steps = [
        (2, 1),
        (2, -1),
        (-2, 1),
        (-2, -1),
        (1, 2),
        (1, -2),
        (-1, 2),
        (-1, -2),
    ]

    answer = 0
    for step in steps:
        cur_col = col + step[0]
        cur_row = row + step[1]
        if cur_col <= 0 or cur_col >= 9 or cur_row <= 0 or cur_col >= 9:
            continue
        else:
            answer += 1

    print(answer)
    return answer


solution("a1")
