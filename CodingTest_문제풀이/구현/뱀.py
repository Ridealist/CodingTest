"""
https://www.acmicpc.net/problem/3190
"""

n = int(input())
game = [[0 for _ in range(n+2)] for _ in range(n+2)]

for i in range(n+2):
    game[0][i] = 3

for i in range(n+2):
    game[-1][i] = 3

for row in game[1:-1]:
    row[0] = 3
    row[-1] = 3

print(game)

apple = int(input())
for _ in range(apple):
    a, b = list(map(int, input().split()))
    game[a][b] = 2


# print(game)

t = int(input())
turn = dict()
for _ in range(t):
    a, b = input().split()
    turn[int(a)] = b

print(game)
print(turn)


def gameover(game, turn):
    


def 


while 