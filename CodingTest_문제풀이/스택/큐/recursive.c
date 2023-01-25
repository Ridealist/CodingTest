#include <stdio.h>

void recursive(int n) {
    if (n == 100) {
        printf("%d번째 재귀 함수를 종료합니다.\n", n);
        return;   
    }
    printf("%d번째 재귀 함수에서 %d번째 재귀 함수를 호출합니다.\n", n, n + 1);
    recursive(n + 1);
    printf("%d번째 재귀 함수를 종료합니다.\n", n);
}

int main() {
    recursive(1);

    return 0;
}