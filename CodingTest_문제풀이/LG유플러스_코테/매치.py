cnt = 0

def countzero(players):
    
    global cnt
    
    flag = False
    
    n = len(players)
    if n == 1:
        return players
    
    l = [0 for _ in range(n//2)]

    for i in range(0, n, 2):
        if players[i] == 0 and players[i+1] == 0:
            l[i//2] = 0
            flag = True
        else:
            l[i//2] = 1
            cnt += 1
    
    # print(players, flag)
    if flag:
        cnt += 1
    return countzero(l)

def solution(players):

    countzero(players)

    return cnt

print(countzero([1,0,0,1,0,0,1,0]))

print(cnt)