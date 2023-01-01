#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>
using namespace std;

int arr[101][100001];

int main() {
  ios::sync_with_stdio(false);
	cin.tie(0);

  int n, k, v, w;
  cin >> n >> k;
  vector <pair<int, int>> vv;
  
  for(int i=0; i<n; i++) {
    cin >> v >> w;
    vv.push_back(make_pair(v, w));
  }

  for (int i = 1; i <= n; i++) {
		for (int j = 1; j <= k; j++) {
			int curweight = vv[i-1].first;
			int curval = vv[i-1].second;
			if (curweight <= j) {
				arr[i][j] = max(arr[i - 1][j - curweight] + curval, arr[i - 1][j]);
			}
			else {
				arr[i][j] = arr[i - 1][j];
			}
		}
	}
	cout << arr[n][k];
}
