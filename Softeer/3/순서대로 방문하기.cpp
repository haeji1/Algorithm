#include <stdio.h>
#include <stdbool.h>
#define MAX_NUM 20

int n,m;
int maps[MAX_NUM][MAX_NUM];
int path[MAX_NUM][2];
int result = 0;

// 상하좌우
int dy[4] = {-1,1,0,0};
int dx[4] = {0,0,-1,1};
bool visited[MAX_NUM][MAX_NUM];
// void print(int n, int(*maps)[MAX_NUM]);

void dfs(int y, int x, int depth) {
    // basis part
    if (depth == m) {
        result += 1;
        return;
    }
    else if (y == path[m - 1][0] && x == path[m - 1][1]) {
        return;
    }
    
    // inductive part
    for (int i = 0; i < 4; i++) {
        int ny = y + dy[i];
        int nx = x + dx[i];
        if (0 <= ny && ny < n && 0 <= nx && nx < n && !maps[ny][nx] && !visited[ny][nx]) {
            visited[ny][nx] = true;
            // path에 있는 경로 거쳤다면 depth + 1
            if (ny == path[depth][0] && nx == path[depth][1]) {
                dfs(ny, nx, depth + 1);
            }
            else {
                dfs(ny, nx, depth);
            }
            visited[ny][nx] = false;
        }
    }
    
}

int main() {
    scanf("%d %d",&n,&m);
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            scanf("%d", &maps[i][j]);
        }
    }
    // print(n, maps);
    
    int y, x;
    for (int i = 0; i < m; i++) {
        scanf("%d %d",&path[i][0],&path[i][1]);
        // 알맞는 위치로 변환
        path[i][0]--;
        path[i][1]--;
    }

    // 첫 경로 방문 처리 후 dfs탐색
    visited[path[0][0]][path[0][1]] = true;
    dfs(path[0][0], path[0][1], 1);
    printf("%d", result);
}

// void print(int n, int(*maps)[MAX_NUM]) {
//     for (int i = 0; i < n; i++) {
//         for (int j = 0; j < m; j++) {
//             printf("%d ", maps[i][j]);
//         }
//         printf("\n");
//     }
// }