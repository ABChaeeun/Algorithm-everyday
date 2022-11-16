#include <iostream>
#include <algorithm>
#include <queue>
#include <string>
using namespace std;
#define X first
#define Y second

int board[52][52] = {0,}; // 그려짐 = 1, 안 그려짐 = 0
bool vis[52][52] = {0,}; // 방문하면 1
int t_num, n, m, cabbage,  num; 

int dx[4] = {1,0,-1,0};
int dy[4] = {0,1,0,-1};

int main(void){
  ios::sync_with_stdio(0);
  cin.tie(0);
  cin >> t_num;
  

  while(t_num--){
      num =0;
      for(int i=0; i<52; i++){
          for(int j=0; j<52; j++){
            board[i][j] = 0;
            vis[i][j] = 0;
          }
      }
      cin >> n >> m; 
      cin >> cabbage;
      while(cabbage--){
          int cn, cm;
          cin >> cn >> cm;
          board[cn][cm] = 1;
        }

    queue<pair<int,int> > Q;
  
    for(int i=0; i<n; i++){
        for(int j=0; j<m; j++){
        if(vis[i][j] == 1 || board[i][j] == 0) continue; 
            num++;
            Q.push({i,j});
            vis[i][j] = 1; 
            while(!Q.empty()){ 
                pair<int, int> cur = Q.front(); Q.pop();
                for(int dir=0; dir<4; dir++){
                    int nx = cur.X + dx[dir];
                    int ny = cur.Y + dy[dir];
                    if(nx < 0 || nx >= n || ny < 0 || ny >= m) continue; 
                    if(vis[nx][ny] || board[nx][ny] != 1) continue;
                    vis[nx][ny] = 1;
                    Q.push({nx, ny});
                }
            }
        
        }
    }
    cout << num << "\n";
  }
}
