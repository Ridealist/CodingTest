/*
https://www.acmicpc.net/problem/2178
*/

#include <stdio.h>

int graph[101][101] = { 0, };   // 미로 저장
int q[10001][2] = { 0, }; // 현재 방문한 좌표(x, y) 저장


// 상하좌우 (-1, 0), (1, 0), (0, -1), (0, 1) 이동
int dx[4] = { -1, 1,- 0, 0 };
int dy[4] = { 0, 0, -1, 1 };
int n = 0, m = 0;  // 미로 크기

int bfs() {
    // 큐 front, rear
    int front = 0; int rear = 0;

    // 큐에 처음 (1, 1) 좌표 삽입
    q[front][0] = 1;
    q[front][1] = 1;
    rear++;

    // 큐가 빌 때 까지
    while (front < rear) {
        int x = q[front][0]; // x 좌표
        int y = q[front][1]; // y 좌표
        front++; // front 이동

        for (int i = 0; i < 4; i++) {
            int nx = x + dx[i];
            int ny = y + dy[i];

            // 범위를 벗어나는 경우
            if (nx < 1 || nx > n || ny < 1 || ny > m)
                continue;
            
            // 길이 아닌 경우
            if (graph[nx][ny] != 1)
                continue;
            
            // 이전 칸에서 이동한 칸 수  + 1
            graph[nx][ny] = graph[nx][ny] + 1;

            // 큐에 (nx, ny) 삽입
            q[rear][0] = nx;
            q[rear][1] = ny;
            rear++;
        }
    }
    return graph[n][m];

}