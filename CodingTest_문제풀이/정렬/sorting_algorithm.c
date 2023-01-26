#include <stdio.h>
#define MAX_VALUE 9

int arr[10] = {7, 5, 9, 0, 3, 1, 6, 2, 4, 8};

int arr2[15] = {7, 5, 9, 0, 3, 1, 6, 2, 9, 1, 4, 8, 0, 5, 2};

void selection_sort(int *arr, int size) {
    for (int i = 0; i < size; i++) {
        int min_idx = i;    // 가장 작은 원소의 인덱스. 우선 for loop의 첫번째 index 값으로 초기화
        for (int j = i + 1; j < size; j++) {    // 다음 인덱스 부터 원소 끝까지 비교
            if (arr[j] < arr[min_idx]) {
                min_idx = j;    // looping 돌면서 인덱스를 업데이트함
            }
        }
        int temp = arr[i];  // looping이 끝나면 swap
        arr[i] = arr[min_idx];
        arr[min_idx] = temp;
    }
}

void insertion_sort(int *arr, int size) {
    for (int i = 1; i < size; i++) {    // 1번째 원소는 정렬되어 있다고 가정
        for (int j = i; j > 0; j--) {
            if (arr[j - 1] > arr[j]) {    // 정렬되지 않은 부분부터 비교하면서 한 칸씩 왼쪽으로 이동
                int tmp = arr[j];
                arr[j] = arr[j - 1];
                arr[j - 1] = tmp;
            }
            else    // 자기보다 같거나 작으면, 그 자리에 삽입 
                break;
        }
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

void counting_sort(int *arr, int size, int max_value) {
    // 모든 원소의 값이 0보다 크거나 같다고 가정
    int count[MAX_VALUE + 1] = {0, };

    for (int i = 0; i < size; i++) {
        int value = arr[i];
        count[value]++;
    }

    for (int i = 0; i <= max_value; i++) {
        if (count[i] != 0) {
            for (int j = 0; j < count[i]; j++) {
                printf("%d ", i);
            }    
        }
    }
    printf("\n");
}


int main() {
    // selection_sort(arr, 10);
    
    // insertion_sort(arr, 10);
    
    quick_sort(arr, 0, 9);

    counting_sort(arr2, 15, 9);


    for (int i = 0; i < 10; i++) {
        printf("%d ", arr[i]);
    }
    printf("\n");
    return 0;
}