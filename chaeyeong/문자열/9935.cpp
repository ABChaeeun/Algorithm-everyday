#include <iostream>
#include <vector>
using namespace std;

int main() {
  string s; 
  cin >> s;
	string t; 
  cin >> t;
	vector<char> left;
	int start = 0; 
  int end = s.length() - 1;
  
	while (start <= end) {
		bool tof = true;
		left.push_back(s[start++]);
		if (left.size() >= t.length()) {
			for (int i = 0; i < t.length(); i++) {
				if (t[i] != left[left.size() - t.length() + i]) {
					tof = false;
					break;
				}
			}
			if (tof) {
				for (int i = 0; i < t.length(); i++) {
					left.pop_back();
				}
			}
		}
	}
	if (left.size() == 0) {
		cout << "FRULA" << endl;
	}
	else {
		for (int i = 0; i < left.size(); i++) {
			cout << left[i];
		}
	}
}
