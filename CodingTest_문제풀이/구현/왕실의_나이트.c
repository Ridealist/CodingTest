#include <stdio.h>
#include <stdlib.h>


// char dx[8] = { 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'};
// char dy[8] = { '1', '2', '3', '4', '5', '6', '7', '8'};

int dx[8] = { 2, 2, -2, -2, -1, 1, -1, 1 };
int dy[8] = { 1, -1, 1, -1, -2, -2, 2, 2 };


int main() {
    char position[2];
    int answer = 0;

    scanf("%s", position);

    char x = position[0];
    char y = position[1];

    // int로 나타내는 것도 고려
    // int x = position[0] - 'a' + 1;
    // int y = position[0] - '0';


    for (int i = 0; i < 8; i++) {
        char nx, ny;
        // int nx, ny;
        nx = x + dx[i];
        ny = y + dy[i];
        if (nx < 'a' || nx > 'h' || ny < '1' || ny > '8')
        // if (nx < 0 || nx > 8 || ny < 0 || ny > 8)
            continue;
        answer++;
    }
    
    printf("%d\n", answer);

    return 0;
}