#include <stdio.h>
#define MAX 1000
int m, n;
int dy[] = {-1,1,0,0};
int dx[] = {0,0,-1,1};
int array[MAX][MAX];
int queue[MAX * MAX][2];
int front = 0, rear = 0;
void print(int m, int n, int array[n][m]);

void enqueue(int y, int x) {
    queue[rear][0] = y;
    queue[rear][1] = x;
    rear++;
}

void dequeue(int *y, int *x) {
    *y = queue[front][0];
    *x = queue[front][1];
    front++;
}

int bfs() {
    while (front < rear) {
        int y, x;
        dequeue(&y, &x);

        for (int d = 0; d < 4; d++) {
            int ny = y + dy[d];
            int nx = x + dx[d];
            if (ny >= 0 && ny < n && nx >= 0 && nx < m && array[ny][nx] == 0) {
                array[ny][nx] = array[y][x] + 1;
                enqueue(ny, nx);
            }
        }
    }

    int result = -1;
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            if (array[i][j] == 0) {
                return -1;
            }
            if (array[i][j] > result) {
                result = array[i][j];
            }
        }
    }
    return result - 1;
}

int main() {
    scanf("%d %d",&m,&n);
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            scanf("%d",&array[i][j]);
        }
    }
    // print(m,n, array);

    // 익은 토마토 좌표 enqueue
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            if (array[i][j] == 1) {
                enqueue(i,j);
            }
        }
    }
    printf("%d\n", bfs());
}

void print(int m, int n, int array[n][m]) {
     for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            printf("%d ",array[i][j]);
        }
        printf("\n");
    }
}