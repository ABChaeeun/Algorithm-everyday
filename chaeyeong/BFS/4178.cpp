#include <iostream>
#include <string>
#include <queue>
#include <algorithm>
using namespace std;

const int MAX = 1000;

typedef struct{
  int y, x;
}Dir;

Dir moveDir[4] = { {1, 0}, {-1, 0}, {0, 1}, {0, -1} };

int R, C;
string maze[MAX];
bool visited[MAX][MAX];
pair<int, int> start;
vector<pair<int, int>> fire;

int BFS(void)
{
        queue<pair<int, int>> q;
        q.push(start);
        queue<pair<int, int>> flame;
        for (int i = 0; i < fire.size(); i++)
                 flame.push(fire[i]);
        int result = 0;
        while (!q.empty())
        {
                 //불부터
                 int flameSize = flame.size();
                 for (int i = 0; i < flameSize; i++)
                 {
                         int y = flame.front().first;
                         int x = flame.front().second;
                         flame.pop();
                         for (int i = 0; i < 4; i++)
                         {
                                 int nextY = y + moveDir[i].y;
                                 int nextX = x + moveDir[i].x;
                                 if(0<=nextY && nextY < R && 0 <= nextX && nextX < C)
                                          if (maze[nextY][nextX] == '.' || maze[nextY][nextX] == 'J')
                                          {
                                                  maze[nextY][nextX] = 'F';
                                                  flame.push({ nextY, nextX });
                                          }
                         }
                 }

                 int curSize = q.size();
                 for (int i = 0; i < curSize; i++)
                 {
                         int y = q.front().first;
                         int x = q.front().second;
                         q.pop();
                         if (y == 0 || y == R - 1 || x == 0 || x == C - 1)
                                 return result + 1;
                         for (int i = 0; i < 4; i++)
                         {
                                 int nextY = y + moveDir[i].y;
                                 int nextX = x + moveDir[i].x;
                                 if (0 <= nextY && nextY < R && 0 <= nextX && nextX < C && !visited[nextY][nextX])
                                          if (maze[nextY][nextX] == '.')
                                          {
                                                  visited[nextY][nextX] = true;
                                                  q.push({ nextY, nextX });
                                          }
                         }
                 }
                 result++;
        }
        return -1;
}

int main(void)
{
        ios_base::sync_with_stdio(0);
        cin.tie(0);
        cin >> R >> C;
        
        for (int i = 0; i < R; i++)
        {
                 cin >> maze[i];
                 for (int j = 0; j < maze[i].size(); j++)
                         if (maze[i][j] == 'J')
                                 start = { i, j };
                         else if (maze[i][j] == 'F')
                                 fire.push_back({ i, j });
        }
        int result = BFS();
        if (result == -1)
                 cout << "IMPOSSIBLE\n";
        else
                 cout << result << "\n";
        return 0;
}
