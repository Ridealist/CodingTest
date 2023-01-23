#include <stdio.h>
#include <string.h>


// 이동 방향을 미리 배열로 선언하기
int dx[4] = { 0, 0, -1, 1 };
int dy[4] = { -1, 1, 0, 0 };
char moveType[4] = { 'L', 'R', 'U', 'D' };


int main() {
    int ch, n;
    char direction[100];

    scanf("%d\n", &n);

    int i = 0;
    while ((ch = getchar()) != '\n') {
        if (ch == ' ')
            continue;
        direction[i] = ch;
        i++;
    }
    direction[i] = '\0';

    int x = 1;
    int y = 1;

    int l = strlen(direction);
    for (int i = 0; i < l; i++) {

        char dist = direction[i];

        // 이동 후 좌표 구하기
        // 이동이 불가할 수 있으니 tmp 파일처럼 우선 생성
        int nx, ny;
        for (int j = 0; j < 4; j++) {
            if (dist == moveType[j]) {
                nx = x + dx[j];
                ny = y + dy[j];
            }
        }

        // 예외사항 처리
        if (nx > n || nx < 1 || ny > n || ny < 1)
            continue;
        
        // 예외사항에 해당 안될경우 새로운 좌표를 할당
        x = nx;
        y = ny;


/*         if (second < n && direction[i] == 'R')
            second += 1;
        else if (second > 1  && direction[i] == 'L')
            second -= 1;
        else if (first < n && direction[i] == 'D')
            first += 1;
        else if (first > 1 && direction[i] == 'U')
            first -= 1; */
    }

    printf("%d %d\n", x, y);



    return 0;
}