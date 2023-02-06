/*
https://www.acmicpc.net/problem/2667
*/

#include <stdio.h>
#include <stdbool.h>
#define MAX_SIZE 25

int n;

int map[MAX_SIZE][MAX_SIZE] = {0, };


int cnt = 0;
int cnt_arr[100] = {0, };

int counting_sort[MAX_SIZE * MAX_SIZE + 1];

bool dfs(int x, int y) {
    // 범위를 벗어나면 즉시 종료
    if (x < 0 || x > n - 1 || y < 0 || y > n - 1)
        return false;
    // 탐색중인 지도가 0이면 즉시 종료
    if (map[x][y] == 0)
        return false;
    
    map[x][y] = 0;
    cnt++;

    dfs(x - 1, y);
    dfs(x + 1, y);
    dfs(x, y + 1);
    dfs(x, y - 1);
    return true;
}

void sort(int *arr, int len) {
    for (int i = 0; i < len - 1; i++) {
        for (int j = i + 1; j < len; j++) {
            if (arr[i] > arr[j]) {
                int tmp = arr[i];
                arr[i] = arr[j];
                arr[j] = tmp;
            }
        }
    }
}

int main() {
    scanf("%d", &n);
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            scanf("%1d", &map[i][j]);
            // map[i] + j -> 이런 형태로 포인터 덧셈 구현 가능 (& 주소 연산자 붙일 필요 없음)
            // scanf("%1d", map[i] + j)
        }
    }

    int idx = 0;

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            if (dfs(i, j)) {
                cnt_arr[idx] = cnt;

                // 계수정렬 아이디어
                // counting_sort[cnt]++;

                idx++;
                cnt = 0;
            }
        }
    }

    sort(cnt_arr, idx);

    printf("%d\n", idx);
    for (int k = 0; k < idx; k++) {
        printf("%d\n", cnt_arr[k]);
    }

    // for (int i = 0; i < MAX_SIZE * MAX_SIZE + 1; i++) {
    //     if (counting_sort[i] != 0) {
    //         int cnt = counting_sort[i];
    //         for (int j = 0; j < cnt; j++) {
    //             printf("%d\n", i);
    //         }
    //     }
    // }
}
