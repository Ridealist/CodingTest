#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <stdbool.h>
#define MAX_SIZE 1000

int N, M;

int graph[MAX_SIZE][MAX_SIZE];

// int visited[MAX_SIZE][MAX_SIZE] = { 0, };
// -> visited를 따로 두는 순간, 0-1로 칸이 나누어진게 의미 없어짐... 오류!

int dx[4] = {1, -1, 0, 0};
int dy[4] = {0, 0, 1, -1};

void input() {
    scanf("%d %d", &N, &M);
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < M; j++) {
            // %1d라고 해준다면 1글자씩 입력받을 수 있고 %10d라고 해준다면 10글자씩 입력받을 수 있음
            scanf("%1d", &graph[i][j]);
        }
    }
}

void dfs(int x, int y) {
    graph[x][y] = 1;
    for (int i = 0; i < 4; i++) {
        int nx = x + dx[i];
        int ny = y + dy[i];
        if (nx < 0 || ny < 0 || nx > N - 1 || ny > M - 1)
            continue;
        if (graph[nx][ny] == 0) {
            dfs(nx, ny);
        }
    }
}

bool dfs_two(int x, int y) {
    // 주어진 범위를 벗어나면 즉시 종료
    if (x < 0 || y < 0 || x > N -1 || y > M-1)
        return false;
    // 현재 노드를 아직 방문하지 않았다면
    if (graph[x][y] == 0) {
        // 해당 노드 방문 처리
        graph[x][y] = 1;
        // 상, 하, 좌, 우 모두 재귀적으로 호출
        dfs_two(x - 1, y);
        dfs_two(x + 1, y);
        dfs_two(x, y - 1);
        dfs_two(x, y + 1);
        return true;
    }
    return false;
}


int main(void) {
    int answer = 0;

    input();
    // 모든 노드(위치)에 대해서 음료수 채우기
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < M; j++) {
            if (graph[i][j] == 1)
                continue;
            dfs(i, j);
            answer++;
        }
    }

/*     for (int i = 0; i < N; i++) {
        for (int j = 0; j < M; j++) {
            if (dfs_two(i, j))
                answer++;;
        }
    } */

    printf("%d\n", answer);

    return 0;
}