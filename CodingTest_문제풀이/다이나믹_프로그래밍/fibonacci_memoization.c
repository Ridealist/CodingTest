#include <stdio.h>

long long memo[100] = {0, };

long long fibo(int n) {
    if (n == 1 || n == 2) {
        return (long long)1;
    }
    // 이미 계산한 적이 있는 문제라면 그대로 반환
    if (memo[n] != 0)
        return memo[n];
    // 아직 계산하지 않은 문제라면 결과 반환해 메모리에 저장
    memo[n] = fibo(n - 1) + fibo(n - 2);
    // 메모리 저장된 값 반환
    return memo[n];
}

// 탑다운(Top Down) 방식
int main(void) {

    long long result = fibo(60);
    printf("%lld\n", result);

    return 0;
}