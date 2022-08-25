import sys
# 표준입력을 파일로 설정

# input() 사용자 입력 받지 않고, 표준입력에 정의된 파일 읽음
n,m = map(int, sys.stdin.readline().split())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(m)]

cnt = 0
for i in range(n):
    s = 0
    while s < m:
        for j in arr[i:]:
            s += j
    if s == m:
        cnt += 1

print(cnt)