#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <stdlib.h>

typedef struct student {
    // TODO char*로 선언된 필드는 scanf값을 입력 받을 수 없다... (저장할 공간이 없기 때문...)
    char name[101];
    int score;
} Student;

int n;
Student students[10000];


typedef struct node {
    Student *data;
    struct node *next;
} Node;


Node *sort[101];


void input() {
    scanf("%d", &n);
    for (int i = 0; i < n; i++) {
        scanf("%s %d", students[i].name, &students[i].score);
    }
}

int main() {

    input();
    for (int i = 0; i < n; i++) {
        Node *node = (Node *)malloc(sizeof(Node));
        node->data = &students[i];
        node->next = NULL;

        Node *p = sort[students[i].score];
        if (p == NULL) {
            sort[students[i].score] = node;
            continue;
        }

        // TODO 다음 노드로 가는 알고리즘 잘 설계하기! 2개의 포인터로 하지 않으면 null에 node가 연결되어 버림.
        Node *q;
        while (p != NULL) {
            q = p;
            p = p->next;
        }
        q->next = node;
    }

    for (int i = 100; i >= 0; i--) {
        Node *node = sort[i];
        while (node != NULL) {
            printf("%s ", node->data->name);
            node = node->next;
        }
    }
    printf("\n");

    return 0;
}