/*
https://www.acmicpc.net/problem/11047
*/

#include <stdio.h>

int size;
int amount;
int answer;

int main() {
    scanf("%d %d", &size, &amount);
    
    int money[size];
    for (int i = 0; i < size; i++) {
        scanf("%d", &money[i]);
    }
    
    for (int j = size - 1; j >= 0; j--) {
        if (money[j] > amount)
            continue;
        answer += amount / money[j];
        amount = amount % money[j];
    }
    
    printf("%d\n", answer);
    
    return 0;
}