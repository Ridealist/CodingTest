#include<stdio.h>

int size = 9;

int visited[9] = { 0, };
int graph[9][9] = { 0, };

int q[10000] = { 0, };

void bfs(int cur) {
    int front = 0;
    int rear = 0;
    // printf("front : %d / rear : %d\n", front, rear);
    q[front] = cur;
    rear++;
    // printf("front : %d / rear : %d\n", front, rear);

    visited[cur] = 1;

    while (front < rear) {
        int pop = q[front];
        front++;
        // printf("front : %d / rear : %d\n", front, rear);
        printf("%d ", pop);
        
        for (int i = 0; i < size; i++) {
            if (graph[pop][i] == 1 && visited[i] == 0) {
                q[rear] = i;
                rear++;
                // printf("front : %d / rear : %d\n", front, rear);
                visited[i] = 1;
            }
        }
    }
}


int main() {

    graph[1][2] = 1; graph[1][3] = 1; graph[1][8] = 1;
    graph[2][1] = 1; graph[2][7] = 1;
    graph[3][1] = 1; graph[3][4] = 1; graph[3][5] = 1;
    graph[4][3] = 1; graph[3][4] = 1;
    graph[5][3] = 1;
    graph[6][7] = 1;
    graph[7][2] = 1; graph[7][6] = 1; graph[7][8] = 1;
    graph[8][1] = 1; graph[8][7] = 1;

    int start = 1;
    bfs(start);

    return 0;
}