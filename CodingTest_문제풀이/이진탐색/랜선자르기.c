/*
https://www.acmicpc.net/problem/1654
*/

#include <stdio.h>

int k, n;
int lan[10000];


int main() {
    int max = 0;
    long long max_len = 0;

    scanf("%d %d", &k, &n);
    for (int i = 0; i < k; i++) {
        scanf("%d", &lan[i]);
        if (lan[i] > max)
            max = lan[i];
    }

    long long start = 1;  // TODO -> 시작값도 1로 만들어야 한다. 같은 길이로 만드는 것인데 길이 0이 가능할 수 없다...!
    long long end = max;
    while (start <= end)
    {
        int count = 0;
        long long mid = (start + end) / 2;  // TODO start + end -> int 범위를 초과할 수 있다.(길이 <= 2^31-1)
                                            // long long 자료형으로 선언해야 자료형 범위를 초과하지 않는다.

        for (int i = 0; i < k; i++) {
            if (lan[i] >= mid)
                count += lan[i] / mid;  // 더욱이, start = 0으로 설정하면 mid가 0이 되버리는 경우도 존재함.
        }
        if (count >= n) {  // TODO mid가 현재 max_len보다 클 때만 값 update
            start = mid + 1;
            if (max_len < mid)
                max_len = mid;
        }
        else
            end = mid - 1;
    }   
    
    printf("%lld\n", max_len);

    return 0;
}
