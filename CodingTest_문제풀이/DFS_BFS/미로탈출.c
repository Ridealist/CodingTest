#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#define MAX_SIZE 200

int n, m;
int graph[MAX_SIZE][MAX_SIZE];

int q[MAX_SIZE][2];
int front = 0, rear = 0;

int dx[4] = {1, -1, 0, 0};
int dy[4] = {0, 0, 1, -1};

void input() {
    scanf("%d %d", &n, &m);
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            scanf("%1d", &graph[i][j]);
        }
    }
}

void bfs(int x, int y) {
    q[rear][0] = x;
    q[rear][1] = y;
    rear++;
    graph[x][y] = 1;
    printf("지나간 곳 x: %d , y: %d\n", x, y);

    // 큐가 빌 때까지 반복
    while (front < rear)
    {
        int *pop = q[front];
        front++;
        for (int i = 0; i < 4; i++) {
            int nx = pop[0] + dx[i];
            int ny = pop[1] + dy[i];
            if (nx < 0 || ny < 0 || nx > n - 1 || ny > m - 1)
                continue;
            // 벽인 경우 무시
            // if (graph[nx][ny] == 0)
            //     continue;

            // 1. 내 방법 -> 누적합으로 구하고 조건문으로 break 시킴
            if (graph[nx][ny] == 1) {
                q[rear][0] = nx;
                q[rear][1] = ny;
                rear++;
                graph[nx][ny] += graph[pop[0]][pop[1]];
                printf("지나간 곳 x: %d , y: %d\n", nx, ny);

                if (nx == n - 1 && ny == m - 1)
                    return; 
            }
            // 2. 교재 방법 -> 처음 방문하는 경우만 거리 기록 (끝까지 루프 돌림)
            // 해당 노드를 처음 방문하는 경우에만 최단 거리 기록
            if (graph[nx][ny] == 1) {
                q[rear][0] = nx;
                q[rear][1] = ny;
                rear++;
                graph[nx][ny] = graph[pop[0]][pop[1]] + 1;
                printf("지나간 곳 x: %d , y: %d\n", nx, ny);
            }
        }
    }
}


int main() {
    input();
    bfs(0, 0);
    printf("%d\n", graph[n - 1][m - 1]);
    return 0;
}