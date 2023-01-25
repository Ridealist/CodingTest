/*
https://wonsjung.tistory.com/9
*/

#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
// 자료구조 생성을 위한 상수값 선언
#define MAX_SIZE 101

// 전역변수 초기 설정
int N, M;
int graph[MAX_SIZE][MAX_SIZE] = { 0, };
int visited[MAX_SIZE] = { 0, };

// Queue 자료구조 전역변수 선언
int q[MAX_SIZE];
int front = 0, rear = 0;

int answer = 0;

// queue 기본 기능 함수 정의
void enque(int x) {
    q[rear] = x;
    rear = (rear + 1) % MAX_SIZE;
}

int deque(int x) {
    int tmp = q[front];
    front = (front + 1) % MAX_SIZE;
    return tmp;
}

int is_empty() {
    if (front == rear)
        return 1;
    return 0;
}

void bfs(int start) {
    enque(start);
    visited[start] = 1;
    while (!is_empty()) {
        int pop = deque(start);
        for (int i = 1; i <= N; i++) {
            if (graph[pop][i] == 1 && visited[i] == 0) {
                enque(i);
                visited[i] = 1;
                answer++;
            }
        }
    }
    
}

// 입력 부분 별도 함수화
void input() {
    scanf("%d", &N);
	scanf("%d", &M);
	for (int i = 0; i < M; i++) {
        int u, v;
		scanf("%d %d", &u, &v);
		graph[u][v] = 1;
		graph[v][u] = 1;
	}
}

int main(void) {
    input();
    bfs(1);
    printf("%d\n", answer);
    return 0;
}