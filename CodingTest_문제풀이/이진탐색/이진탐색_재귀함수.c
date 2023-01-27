#include <stdio.h>

int binary_search(int arr[], int target, int start, int end) {
    // 못찾으면 -1 반환
    if (start > end)
        return -1;
    // 찾은 경우 중간점 인덱스 반환
    int mid = (start + end) / 2;
    if (arr[mid] == target)
        return (mid + 1);
    // 중간점의 값보다 찾고자 하는 값이 큰 경우 오른쪽 확인
    else if (arr[mid] < target)
        return binary_search(arr, target, mid + 1, end);
    // 중간점의 값보다 찾고자 하는 값이 작은 경우 왼쪽 확인
    else
        return binary_search(arr, target, start, mid - 1); 
}

int main() {

    int arr[13] = {1, 3, 4, 5, 6, 8, 9, 10, 11, 12, 14, 15};

    int answer = binary_search(arr, 18, 0, 15);

    printf("%d\n", answer);

    return 0;
}