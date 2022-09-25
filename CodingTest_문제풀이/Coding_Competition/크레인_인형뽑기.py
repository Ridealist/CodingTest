"""
https://school.programmers.co.kr/learn/courses/30/lessons/64061
"""

### 내 풀이
def solution(board, moves):
    answer = 0
    repo = []
    for move in moves:
        catch = None
        for b in board:
            if b[move - 1] == 0:
                continue
            else:
                catch = b[move - 1]
                b[move - 1] = 0
                break
        print(catch)
        if catch:
            if len(repo) >= 2:
                if catch == repo[-1]:
                    repo.pop(-1)
                    answer += 2
            else:
                repo.append(catch)
    print(repo)
    return answer


def Compare(repo, catch):
    repo.append(catch)
    if len(repo) >= 2:
        if repo[-1] == repo[-2]:
            repo.pop(-1)
            repo.pop(-1)
            answer += 2
    return repo, answer


### 회택 풀이
def solution(board, moves):
    # transpose
    t_board = [list(i) for i in zip(*board)]

    st = []
    cnt = 0
    # moves - 1 만큼씩 빼기
    for move in moves:
        print(f"move is {move - 1}")
        line = t_board[move - 1]
        print(f"line is {line}")
        for i in range(len(line)):
            if line[i] != 0:
                print(line[i])
                # stack 만들어서 동일한 게 들어가면 pop 하기
                if st and st[-1] == line[i]:
                    st.pop()
                    cnt += 2
                else:
                    st.append(line[i])
                line[i] = 0
                print(st)
                break

    return cnt


###홍동쌤 풀이
def solution(board, moves):
    st = []
    answer = 0
    for move in moves:
        doll = None
        idx = move - 1
        for b in board:
            if b[idx] == 0:
                continue
            else:
                doll = b[idx]
                b[idx] = 0
                if len(st) == 0:
                    st.append(doll)
                else:
                    if st[-1] == doll:
                        st.pop(-1)
                        answer += 2
                    else:
                        st.append(doll)
                break
    return answer
