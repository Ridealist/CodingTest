#include <stdio.h>
#define INF 999999999  // 무한 비용 선언

int graph[3][3] = {
    { 0, 7, 5 },
    { 7, 0, INF},
    { 5, INF, 0}
};

int main() {
    for (int i = 0; i < 3; i++) {
        for (int j = 0; j < 3; j++) {
            printf("%d ", graph[i][j]);
        }
        printf("\n");
    }

    return 0;
}
