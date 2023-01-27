#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>
#define MAX_SIZE 1000000

int n, m;
int directory[MAX_SIZE];
int order[MAX_SIZE];


bool binary_search(int arr[], int target, int start, int end) {
    if (end < start)
        return false;
    
    int mid = (start + end) / 2;

    if (arr[mid] == target)
        return true;
    else if (arr[mid] > target)
        return binary_search(arr, target, start, mid - 1);
    else
        return binary_search(arr, target, mid + 1, end);
}

void input() {
    scanf("%d", &n);
    for (int i = 0; i < n; i++) {
        scanf("%d", &directory[i]);
    }
    scanf("%d", &m);
    for (int i = 0; i < m; i++) {
        scanf("%d", &order[i]);
    }
}

int compare(const void *a, const void *b) {

    return *(int *)a - *(int *)b;
}


int main() {

    input();
    qsort(directory, n, sizeof(int), compare);

    for (int i = 0; i < m; i++) {
        bool flag = binary_search(directory, order[i], 0, n-1);
        if (flag)
            printf("yes ");
        else
            printf("no ");
    }
    printf("\n");

    return 0;
}