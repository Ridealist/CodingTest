/*
https://www.acmicpc.net/problem/11399
*/

#include <stdio.h>
#include <stdlib.h>

int compare(const void *a, const void *b) {
    if (*(int *)a > *(int *)b)
        return 1;
    else if (*(int *)a == *(int *)b)
        return 0;
    else
        return -1;
}


int main() {
    int K;
    int answer = 0;
    scanf("%d", &K);

    int time[K];
    for (int i = 0; i < K; i++) {
        scanf("%d", &time[i]);
    }

    qsort(time, K, sizeof(int), compare);

    int pre = 0;
    int now;
    for (int i = 0; i < K; i++) {
        now = pre + time[i];
        answer += now;
        pre = now;
    }
/*     for (int i = 0; i < K; i++) {
        answer += (K - i) * time[i];
    } */

    printf("%d", answer);

    return 0;
}