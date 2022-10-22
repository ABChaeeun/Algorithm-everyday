#include <iostream>
#include <string.h>
using namespace std;

int m, n;
int tb[501][501];
int dp[501][501]{ 0, };
int isinside[4][2] = { {0,1} ,{1,0}, {0,-1},{-1,0} };
int dpR(int y,int x) {

	if (dp[y][x] != -1) return dp[y][x];
	if (y<1 || y>m || x<1 || x>n) return 0;
	if (y == 1 && x == 1)return 1;

	dp[y][x] = 0;
	for (int i = 0; i < 4; i++) {
		int dy = y + isinside[i][0];
		int dx = x + isinside[i][1];
		if (tb[dy][dx]>tb[y][x]) {
			dp[y][x] += dpR(dy, dx);
		}
	}
	return dp[y][x];
}

int main() {
  cin >> m >> n;
	for (int i = 1; i <= m; i++) {
		for (int j = 1; j <= n; j++) {
			cin >> tb[i][j];
		}
	}
	memset(dp, -1, sizeof(dp));
	cout << dpR(m, n) << endl;
}
