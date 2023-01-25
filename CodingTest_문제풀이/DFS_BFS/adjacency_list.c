
/*
https://mangoreview.tistory.com/entry/C%EC%96%B8%EC%96%B4-%EC%97%B0%EA%B2%B0-%EC%9E%90%EB%A3%8C%EA%B5%AC%EC%A1%B0%EB%A5%BC-%EC%9D%B4%EC%9A%A9%ED%95%9C-%EA%B7%B8%EB%9E%98%ED%94%84-%EA%B5%AC%ED%98%84%EB%8B%A8%EC%88%9C%EC%97%B0%EA%B2%B0-%EB%A6%AC%EC%8A%A4%ED%8A%B8
*/


#include <stdio.h>
#include <stdlib.h>
#define MAX_VERTEX 30

typedef struct graphNode {
	int vertex;
	struct graphNode* link;
}graphNode;

typedef struct graphType {
	int n;
	graphNode* adjList_H[MAX_VERTEX];
}graphType;

void createGraph(graphType* g) {
	g->n = 0;
	for (int v = 0; v < MAX_VERTEX; v++) {
		g->adjList_H[v] = NULL;
	}
}

void insertVertex(graphType* g, int v) {
	if (((g->n) + 1) > MAX_VERTEX) {
		printf("그래프 정점의 개수를 초과하였습니다(최대 개수:%d 입니다)\n", MAX_VERTEX);
		return;
	}
	g->n++; //g->n의 값을 1늘린다는것은 정점의 개수를 한개 늘린다는 뜻이다.
}

void insertEdge(graphType* g, int u, int v) {
	graphNode* node;
	if (u >= g->n || v >= g->n) {
		printf("[ 그래프에 없는 정점입니다 ]\n");
		return;
	}
	node = (graphNode*)malloc(sizeof(graphNode));
	node->vertex = v;
	node->link = g->adjList_H[u];
	g->adjList_H[u] = node;
}

void print_adjList(graphType* g) {
	int i;
	graphNode* p;
	for (i = 0; i < g->n; i++) {
		printf(" \n정점 %c 의 인접 리스트 : %c ", i + 65,i+65);
		p = g->adjList_H[i];
		while (p) {
			printf(" -> %c", p->vertex + 65);
			p = p->link;
		}
	}
}

int main() {
	int i;
	graphType* G1;
	G1 = (graphType*)malloc(sizeof(graphType));
	createGraph(G1);

	for (i = 0; i < 4; i++) {
		insertVertex(G1, i); //G1에 정점 4개 추가하기
	}
	insertEdge(G1, 0, 3);insertEdge(G1, 0, 1);
	insertEdge(G1, 1, 3);insertEdge(G1, 1, 2); insertEdge(G1, 1, 0);
	insertEdge(G1, 2, 3);insertEdge(G1, 2, 1);
	insertEdge(G1, 3, 2);insertEdge(G1, 3, 1); insertEdge(G1, 3, 0);

	printf("[ G1의 인접 리스트 ]");
	print_adjList(G1);
    printf("\n");
}