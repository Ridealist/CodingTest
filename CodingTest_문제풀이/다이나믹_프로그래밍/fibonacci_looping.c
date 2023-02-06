#include <stdio.h>

long long d[100] = { 0, };


// 보텀업(Bottom Up) 방식
int main() {
    
    d[1] = (long long)1;
    d[2] = (long long)1;
    int n = 60;

    for (int i = 3; i <= n; i++) {
        d[i] = d[i - 1] + d[i - 2];
    }

    printf("%lld\n", d[60]);

    return 0;
}