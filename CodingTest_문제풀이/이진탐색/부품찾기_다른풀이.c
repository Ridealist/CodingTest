#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>
#define MAX_SIZE 1000000

int n, m;
int counting[MAX_SIZE + 1] = {0,};  // TODO 계수 정렬에서 배열의 크기는 "MAX_VALUE + 1"!!

int order[MAX_SIZE];

// 1. 계수정렬
void input() {
    scanf("%d", &n);
    for (int i = 0; i < n; i++) {
        int k;
        scanf("%d", &k);
        counting[k]++;
    }
    scanf("%d", &m);
    for (int i = 0; i < m; i++) {
        scanf("%d", &order[i]);
    }
}

int main() {

    input();

    for (int i = 0; i < m; i++) {
        if (counting[order[i]] != 0)
            printf("yes ");
        else
            printf("no ");
    }
    printf("\n");

    return 0;
}