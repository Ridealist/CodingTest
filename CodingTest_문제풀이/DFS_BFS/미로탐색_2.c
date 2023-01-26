#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#define MAX_SIZE 101

int n, m;
// map 초기화
int maze[MAX_SIZE][MAX_SIZE] = { 0, };

// TODO q의 stackoverflow 주의!!!
// 사이즈가 작은 큐는 기계 채점에서 오류 발생!!!
// int q[MAX_SIZE][2]; -> 너무 작은 사이즈
int q[10000][2] = { 0, };
// 큐 초기화
int front = 0, rear = 0;

int dx[] = {1, -1, 0, 0};
int dy[] = {0, 0, 1, -1};

void input() {
    scanf("%d %d", &n, &m);
    for (int i = 1; i <= n; i++) {
        for (int j = 1; j <= m; j++) {
            scanf("%1d", &maze[i][j]);
        }
    }
}

void bfs(int x, int y) {
    q[rear][0] = x;
    q[rear][1] = y;
    rear++;

    while (front < rear) {
        int *pop = q[front];
        int x = pop[0];
        int y = pop[1];
        front++;
        for (int i = 0; i < 4; i++) {
            int nx = x + dx[i];
            int ny = y + dy[i];
            if (nx < 1 || ny < 1 || nx > n || ny > m)
                continue;
            if (maze[nx][ny] == 0)
                continue;
            if (maze[nx][ny] == 1) {
                q[rear][0] = nx;
                q[rear][1] = ny;
                rear++;

                maze[nx][ny] += maze[x][y];

                printf("x: %d , y: %d\n", nx, ny);

                if (nx == n && ny == m)
                    return;
            }
        }
        maze[x][y] = 0;
    }
}


int main(void) {
    input();

    printf("\n");
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            printf("%d", maze[i][j]);
        }
        printf("\n");
    }

    bfs(1, 1);
    printf("%d\n", maze[n][m]);
    return 0;
}