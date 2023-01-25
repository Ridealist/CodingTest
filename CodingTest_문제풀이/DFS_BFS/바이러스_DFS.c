/*
https://www.acmicpc.net/problem/2606
*/

#include <stdio.h>

int N, M;

int answer = 0;

int graph[101][101];
int visited[101];

void dfs(int cur) {
    visited[cur] = 1;
    answer++;
    for (int i = 1; i <= N; i++) {
        if (graph[cur][i] == 1 && visited[i] == 0)
            dfs(i);
    }
}

int main() {

    scanf("%d", &N);
    scanf("%d", &M);

    for (int i = 0; i < M; i++) {
        int u, v;
        scanf("%d %d", &u, &v);
        graph[u][v] = 1;
        graph[v][u] = 1;
    }

    dfs(1);
    printf("%d\n", answer - 1);

    return 0;
}