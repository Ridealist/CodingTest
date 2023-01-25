/*
https://www.acmicpc.net/problem/2606
*/

#include <stdio.h>

int computer_cnt;

int answer = 0;
int q[1000] = { 0, };

int graph[100][100] = { 0, };
int visited[100] = { 0, };

void bfs(int start) {
    int front = 0;
    int rear = 0;

    // queue는 후단(rear) 삽입, 전단(front) 인출이 원칙
    q[rear] = start;
    visited[start] = 1;
    rear++;

    while (front < rear) {
        int pop = q[front];
        front++;
        // printf("infected : %d\n", pop);

        for (int i = 1; i <= computer_cnt; i++) {
            if (graph[pop][i] == 1 && visited[i] == 0) {
                q[rear] = i;
                rear++;
                visited[i] = 1;
                answer++;
            }
        }
    }
};


int main() {
    int iter;

    scanf("%d", &computer_cnt);
    scanf("%d", &iter);

    for (int i = 0; i < iter; i++) {
        int x;
        int y;
        scanf("%d %d", &x, &y);
        graph[x][y] = 1;
        graph[y][x] = 1;
    }

    bfs(1);

    printf("%d\n", answer);

    return 0;
}