#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <stdlib.h>

int n;
int arr[500];

void input() {
    scanf("%d", &n);
    for (int i = 0; i < n; i++) {
        scanf("%d", arr + i);
    }
}


void decending_quick_sort(int *arr, int start, int end) {
    if (start >= end)
        return;
    
    int pivot = start;
    int left = start + 1;
    int right = end;

    while (left <= right) {
        while (left <= end && arr[left] >= arr[pivot])
            left++;
        while (right > start && arr[right] <= arr[pivot])
            right--;
        if (left > right) {
            int tmp = arr[right];
            arr[right] = arr[pivot];
            arr[pivot] = tmp;
        }
        else {
            int tmp = arr[right];
            arr[right] = arr[left];
            arr[left] = tmp;
        }
    }
    decending_quick_sort(arr, start, right - 1);
    decending_quick_sort(arr, right + 1, end);
}


int main() {
    input();
    decending_quick_sort(arr, 0, n - 1);
    for (int i = 0; i < n; i++) {
        printf("%d ", arr[i]);
    }
    printf("\n");
    
    return 0;
}