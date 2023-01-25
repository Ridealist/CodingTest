#include <stdio.h>

int size = 9;

int graph[9][9] = { 0, };
int visited[9] = { 0, };

void dfs(int cur) {
    printf("%d ", cur);
    visited[cur] = 1;  // 현재 노드를 방문처리

    for (int i = 0; i < size; i++) {   // 모든 인접한 노드 체크
        if (graph[cur][i] == 1 && visited[i] == 0)
            dfs(i);
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

    // int graph[][] = {
    //     {},
    //     { 2, 3, 8 },
    //     { 1, 7 },
    //     { 1, 4, 5 },
    //     { 3, 5 },
    //     { 3, 4 },
    //     { 7 },
    //     { 2, 6, 8 },
    //     { 1, 7}
    // };


    int start = 1;
    dfs(start);

    return 0;
}