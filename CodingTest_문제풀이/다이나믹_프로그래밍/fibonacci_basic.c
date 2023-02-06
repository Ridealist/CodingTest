#include <stdio.h>

long long fibo(int n) {
    if (n == 1 || n == 2) {
        return (long long)1;
    }
    
    return fibo(n - 1) + fibo(n - 2);
}

int main(void) {

    long long result = fibo(50);
    printf("%lld\n", result);

    return 0;
}