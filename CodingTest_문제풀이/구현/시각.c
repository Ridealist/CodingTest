#include <stdio.h>
#include <string.h>
#include <stdbool.h>

bool check(int h, int m, int s) {
    if (h % 10 == 3 || m / 10 == 3 || m % 10 == 3 || s / 10 == 3 || s % 10 == 3) {
        return true;
    }
    return false;
}


int main() {
    int n;
    int answer;

    scanf("%d", &n);

    // 여집합
    if (n < 3) {
        answer = ((n + 1) * 6 * 10 * 6 * 10) - ((n + 1) * 5 * 9 * 5 * 9);
    }
    else if (n >= 3 && n < 13) {
        answer = ((n + 1) * 6 * 10 * 6 * 10) - (n * 5 * 9 * 5 * 9);
    }
    if (n >= 13 && n < 23) {
        answer = ((n + 1) * 6 * 10 * 6 * 10) - ((n - 1) * 5 * 9 * 5 * 9);
    }
    if (n == 23) {
        answer = ((n + 1) * 6 * 10 * 6 * 10) - ((n - 2) * 5 * 9 * 5 * 9);
    }
    printf("여집합 풀이 정답 : %d\n", answer);


    // 완전 탐색. 브루트 포스. -> 전체 경우의 수가 86,400 / 100,000 10만개도 되지 않으므로
    // 시, 분, 초에 대한 3중 반복문
    int count = 0;
    char hour[10];
    char minute[10];
    char second[10];

    for (int i = 0; i <= n; i++) {
        for (int j = 0; j <= 59; j++) {
            for (int k = 0; k <= 59; k++) {
                sprintf(hour, "%d", i);
                sprintf(minute, "%d", j);
                sprintf(second, "%d", k);

                // 목과 나머지 고려한 check 함수 활용 가능
                // if (check(i, j, k))
                //     count++;;

                if (strstr(hour, "3") != NULL || strstr(minute, "3") != NULL || strstr(second, "3") != NULL)
                    count++;
            }
        }
    }

    printf("브루트 포스 풀이 정답 : %d\n", count);


    return 0;
}