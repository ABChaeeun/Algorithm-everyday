#include<iostream>
#include<queue>
#include<deque>
#include<algorithm>
#include<string.h>
using namespace std;
int N;
int grid[100][100];
int visited[100][100];
int dx[4] = {-1,1,0,0};
int dy[4] = {0,0,-1,1};
 
void bfs(int coin, int nowy, int nowx) {
    queue < pair < int,int > > q;
    q.push(make_pair(nowy,nowx));
    visited[nowy][nowx] = 1;
    while(!q.empty()) {
        int y = q.front().first;
        int x = q.front().second;
        q.pop();
        int color = grid[y][x];
        if(coin == 1) {
            for(int i=0; i<4; i++) {
                int ny = y + dy[i];
                int nx = x + dx[i];
                if(ny >= N || ny < 0 || nx >= N || nx < 0)
                    continue;
                if(visited[ny][nx])
                    continue;
                if(grid[ny][nx] == color) {
                    visited[ny][nx] = 1;
                    q.push(make_pair(ny,nx));
                }
            }
        }
        else if(coin == 2) {
            for(int i=0; i<4; i++) {
                int ny = y + dy[i];
                int nx = x + dx[i];
                if(ny >= N || ny < 0 || nx >= N || nx < 0)
                    continue;
                if(visited[ny][nx])
                    continue;
                if(color == 3) {
                    if(grid[ny][nx] == color) {
                        visited[ny][nx] = 1;
                        q.push(make_pair(ny,nx));
                    }
                }
                else {
                    if(grid[ny][nx] != 3) {
                        visited[ny][nx] = 1;
                        q.push(make_pair(ny,nx));
                    }
                }
            }
        }
    }
}
 
int main() {
    scanf("%d",&N);
    string word[N];
    for(int i=0; i<N; i++) {
        cin >> word[i];
    }
    for(int i=0; i<N; i++) {
        for(int j=0; j<word[i].size(); j++) {
            if(word[i].at(j) == 'R') grid[i][j] = 1;
            else if(word[i].at(j) == 'G') grid[i][j] = 2;
            else if(word[i].at(j) == 'B') grid[i][j] = 3;
 
        }
    }
    int normal = 0;
    int abnormal = 0;
    for(int i=0; i<N; i++) {
        for(int j=0; j<N; j++) {
            if(visited[i][j] == 0) {
                normal++;
                bfs(1,i,j);
            }
        }
    }
    memset(visited,0,sizeof(visited));
    for(int i=0; i<N; i++) {
        for(int j=0; j<N; j++) {
            if(visited[i][j] == 0) {
                abnormal++;
                bfs(2,i,j);
            }
        }
    }
    printf("%d %d\n",normal,abnormal);
}
