#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

typedef struct node {
    int data;
    struct node *next;
} Node;

typedef struct queue {
    Node *front;
    Node *rear;
    int count;  // 큐 안의 노드 개수
} Queue;

void init_queue(Queue *q) {
    q->front = q->rear = NULL;
    q->count = 0;   // 큐 안의 노드 개수를 0으로 설정
}

bool is_empty(Queue *q) {
    return q->count == 0;
    // return q->front == NULL && q->rear == NULL, 조건식도 가능
}

void enqueue(Queue *q, int data) {
    Node *n = (Node *)malloc(sizeof(Queue));
    n->data = data;
    n->next = NULL;

    if (is_empty(q))
        q->front = n;   // 맨 앞을 new Node로 설정
    else
        q->rear->next = n;  // 맨 뒤의 다음을 new Node로 설정

    q->rear = n;    // 맨 뒤를 new Node로 설정
    q->count++; // 큐 안의 노드 개수 1 증가

    printf("queue : (f) ");
    Node *ptr = q->front;
    while (ptr != NULL) {
        printf("%d ", ptr->data);
        ptr = ptr->next;
    }
    printf(" (r)\n");
}

int dequeue(Queue *q) {
    Node *n;
    int data;

    if (is_empty(q)) {
        printf("(Error. Queue is empty.)\n");
        return 0;
    }
    n = q->front;
    data = n->data;
    q->front = n->next;
    free(n);
    q->count--;

    printf("queue : (f) ");
    Node *ptr = q->front;
    while (ptr != NULL) {
        printf("%d ", ptr->data);
        ptr = ptr->next;
    }
    printf(" (r)\n");

    return data;
}

int main(void) {

    int i = 0;
    Queue *q = (Queue *)malloc(sizeof(Queue));
    init_queue(q);

    for (i = 1; i < 5; i++) {
        enqueue(q, i);
    }

    while (!is_empty(q)) {
        dequeue(q);
    }
    dequeue(q);
    dequeue(q);
    enqueue(q, 5);
    enqueue(q, 6);
    enqueue(q, 7);
    dequeue(q);

    return 0;
}