#include <stdio.h>
#include <stdlib.h>

typedef struct {
    int start;
    int end;
} TimeTable;

int compare(const void *a, const void *b) {
    TimeTable A = *(TimeTable *)a;
    TimeTable B = *(TimeTable *)b;
    if (A.end > B.end)
        return 1;
    else if (A.end == B.end) {
        if (A.start > B.start)
            return 1;
        else
            return -1;
    }
    else
        return -1;
}

int main() {
    int K;
    int answer = 0;
    scanf("%d", &K);

    TimeTable table[K];
    for (int i = 0; i < K; i++) {
        scanf("%d %d", &(table[i].start), &(table[i].end));
    }

    qsort(table, K, sizeof(TimeTable), compare);

    TimeTable t = table[0];
    answer += 1;
    for (int i = 1; i < K; i++) {
        if (table[i].start >= t.end) {
            t = table[i];
            answer += 1;
        }
    }
    printf("%d", answer);

    return 0;
}