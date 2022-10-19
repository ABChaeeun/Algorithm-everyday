#include <iostream>
#include <vector>
using namespace std;

int main() {
  vector<int> dp(10001, 0);
  int N; 
  cin >> N;
	vector<int> glass(N + 1, 0);
  
	for (int i = 1; i <= N; i++) {
		cin >> glass[i];
	}
  
	dp[1] = glass[1];
	dp[2] = glass[1] + glass[2];
  
	for (int i = 3; i <= N; i++) {
		dp[i] = max(dp[i - 1], max(dp[i - 2] + glass[i], dp[i - 3] + glass[i - 1] + glass[i]));
	}
  
	cout << dp[N];
}
