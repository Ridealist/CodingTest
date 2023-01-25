#include <stdio.h>
#include <stdbool.h>
#define MAX_STACK_SIZE 100

int stack[MAX_STACK_SIZE];
int top = -1;

bool is_empty() {
    if (top < 0)
        return true;
    return false;
}

bool is_full() {
    if (top >= MAX_STACK_SIZE)
        return true;
    return false;
}

void push(int value) {
    if (is_full()) {
        printf("Error : Stack is full.\n");
        return;
    }
    stack[++top] = value;
    printf("stack : ");
    for (int i = 0; i <= top; i++) {
        printf("%d ", stack[i]);
    }
    printf("\n");
}

int pop() {
    if (is_empty()) {
        printf("Error : Stack is empty.\n");
        return 0;
    }
    int val = stack[top--];
    printf("stack : ");
    for (int i = 0; i <= top; i++) {
        printf("%d ", stack[i]);
    }
    printf("\n");
    return val;
}

int main(void) {

    push(5);
    push(2);
    push(3);
    push(7);
    pop();
    push(1);
    push(4);
    pop();
    pop();
    pop();
    pop();
    pop();
    pop();
    pop();
    push(4);

    return 0;
}