#include <stdio.h>
#include <limits.h>

int n, k;
int arr_a[100000];
int arr_b[100000];

void input() {
    scanf("%d %d", &n, &k);
    for (int i = 0; i < n; i++) {
        scanf("%d", &arr_a[i]);
    }
    for (int i = 0; i < n; i++) {
        scanf("%d", &arr_b[i]);
    }
}


void quick_sort(int *arr, int start, int end) {
    if (start >= end)   // 원소가 1개인 경우 종료 - 재귀함수 종료 조건
        return;
    int pivot = start;  // 피벗은 첫 번째 원소
    int left = start + 1;
    int right = end;
    
    while (left <= right) {
        while (left <= end && arr[left] <= arr[pivot])
            left++;
        while (right > start && arr[right] >= arr[pivot])
            right--;
        if (left > right) {   // 엇갈렸다면 작은 데이터와 피벗을 교체
            int tmp = arr[right];
            arr[right] = arr[pivot];
            arr[pivot] = tmp;
        }
        else {  // 엇갈리지 않았다면 작은 데이터와 큰 데이터를 교체
            int tmp = arr[right];
            arr[right] = arr[left];
            arr[left] = tmp;
        }
    }
    // 분할 이후 왼쪽 부분과 오른쪽 부분 각각 정렬 수행
    quick_sort(arr, start, right - 1);
    quick_sort(arr, right + 1, end);
}

// TODO n이 매우 클 수 있으므로 합계도 매우 매우 커질 가능성에 대비해야 함.
// TODO 제한 조건에 맞는 자료형 고려하기!
long long sum(int *arr, int size) {
    long long s = 0;
    for (int i = 0; i < size; i++) {
        s += arr[i];
    }
    return s;
}


int main() {
    input();

    quick_sort(arr_a, 0, n - 1);
    quick_sort(arr_b, 0, n - 1);

    // TODO 오류! 최대 K번 바꿔치기 연산이므로, 단순히 바꿔치기만 하면 안됨. 분기문 설정!
    for (int i = 0; i < k; i++) {
        if (arr_a[i] >= arr_b[n - 1 - i])
            break;
        int tmp = arr_a[i];
        arr_a[i] = arr_b[n - 1 - i];
        arr_b[n - 1 - i] = tmp;
    }

    printf("%lld\n", sum(arr_a, n));

    return 0;
}