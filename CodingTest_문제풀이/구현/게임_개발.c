#include <stdio.h>

int n, m, x, y, direction;

// 방문할 위치를 저장하기 위한 맵을 생성하여 0으로 초기화
int d[50][50] = { 0, };
// 전체 맵 정보
int arr[50][50];

// 방향을 설정해서 이동하는 문제 유헝 -> dx, dy 리스트 만들어 방향 정하면 효과적!
// 북 : 0, 동 : 1, 남 : 2, 서 : 3 방향 정의
int dx[] = { -1, 0, 1, 0 };
int dy[] = { 0, 1, 0, -1 };

// 왼쪽 회전
void turn_left() {
    direction -= 1;
    if (direction == -1)
        direction = 3;
}

int main(void) {

    scanf("%d %d", &n, &m);
    scanf("%d %d %d", &x, &y, &direction);
    // 현재 좌표 방문 처리
    d[x][y] = 1;
    int cnt = 1;

    // 전체 맵 정보 입력 받기
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            scanf("%d", &arr[i][j]);
        }
    }

    // 시뮬레이션 시작
    int turn_time = 0;
    while (1) {
        turn_left();
        int nx = x + dx[direction];
        int ny = y + dy[direction];
        
        // 회전한 이후 정면에 가보지 않은 칸이 존재하는 경우 이동
        if (d[nx][ny] == 0 && arr[nx][ny] == 0) {
            d[nx][ny] = 1;
            x = nx;
            y = ny;
            cnt++;
            turn_time = 0;
            continue; 
        }
        // 회전한 이후 정면에 가보지 않은 칸이 없거나, 바다인 경우
        else turn_time += 1;

        // 네 방향 모두 갈 수 없는 경우
        if (turn_time == 4) {
            nx = x - dx[direction];
            ny = y - dy[direction];
            // 뒤로 갈 수 있다면 이동
            if (arr[nx][ny] == 0) {
                x = nx;
                y = ny;
            }
            else
                break;
            turn_time = 0;
        }
    }

    printf("%d", cnt);

}