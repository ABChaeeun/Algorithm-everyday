#include <iostream>
#include <queue>
using namespace std;

int main()
{
	ios::sync_with_stdio(false);
	cin.tie(NULL);

	int n, k;
	cin >> n;
	priority_queue<int> max; // 중간값보다 큼
	priority_queue<int, vector<int>, greater<int>> min; // 중간값보다 작음
	
	for (int i = 1; i <= n; i++) {
		cin >> k;
		if (max.size() == min.size()) max.push(k);
		else min.push(k);
		if (!maxheap.empty() && !min.empty() && min.top() < max.top()) {
			int x = min.top();
			int y = max.top();
			max.pop();min.pop(); 
      max.push(x);min.push(y);
		}
		cout << max.top() << '\n';
	}

	return 0;
}
