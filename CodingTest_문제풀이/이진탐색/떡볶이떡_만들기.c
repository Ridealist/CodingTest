#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>


int n, m;
int arr[1000000];

int sum(int arr[], int size) {
    int s = 0;
    for (int i = 0; i < size; i++) {
        s += arr[i];
    }
    return s;
}

int binary_search_recursive(int arr[], int size, int target, int start, int end) {
    int s = 0;

    if (start > end)
        return -1;
    
    int h = (start + end) / 2;

    for (int i = 0; i < size; i++) {
        int n = arr[i] - h;
        if (n <= 0)
            continue;
        else
            s += n;
    }

    if (s == target)
        return h;
    
    else if (s > target)
        return binary_search_recursive(arr, size, target, h + 1, end);    // TODO 이진탐색 범위 설정 잘하기! 위로 올라갈수록 s가 "작아지는" 것
    else
        return binary_search_recursive(arr, size, target, start, h - 1);    // TODO 이진탐색 범위 설정 잘하기. 아래로 내려올수록 s가 "커지는" 것
}


// 반복문 사용
int binary_search_looping(int arr[], int size, int target, int start, int end) {

    while (start <= end) {
        int h = (start + end) / 2;

        int s = 0;
        for (int i = 0; i < size; i++) {
            int n = arr[i] - h;
            if (n <= 0)
                continue;
            else
                s += n;
        }

        if (s == target)
            return h;
        else if (s > target)
            start = h + 1;
        else
            end = h - 1;
    }
    return -1;
}


int main() {
    int max = 0;
    int result;
    // int end = 1e9; -> // TODO 아주 큰 값으로 초기화도 가능

    scanf("%d %d", &n, &m);
    for (int i = 0; i < n; i++) {
        int x;
        scanf("%d", &x);
        if (x > max)
            max = x;
        arr[i] = x;
    }

    // result = binary_search_looping(arr, n, m, 0, max);

    // TODO 파라메트릭 서치 문제 유형은 (이진 탐색을 재귀적으로 구현하지 않고) 반복문을 이용해 구현하는게 좋음!

    int start = 0;
    int end = max;

    while (start <= end) {
        int h = (start + end) / 2;

        long long total = 0;    // TODO 범위가 벗어날 것 같은 것 자료형 널널하게 선택
        for (int i = 0; i < n; i++) {
            // int n = arr[i] - h;
            // if (n <= 0)
            //     continue;
            // else
            //     total += n;
            if (arr[i] > h)
                total += arr[i] - h;
        }

        if (total == m) {
            result = h;
            break;
        }

        else if (total > m) {
            // 최대한 덜 잘랐을 때가 정답이므로, 여기에 result값을 기록
            result = h;
            start = h + 1;
        }
        else
            end = h - 1;
    }

    // printf("%d\n", max);
    printf("%d\n", result);

    return 0;
}