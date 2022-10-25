#include <iostream>
using namespace std;

int main() {
  int hu[5][4]; 
  int mx = 0;
  for (int i = 0; i < 5; i++) {
    for (int j = 0; j < 4; j++) {
      cin >> hu[i][j];
      if (i == 0) {
        mx += hu[i][j];
      }
    }
  }
  int win[5];   
  int idx = 0;

  for (int i = 0; i < 5; i++) {
    int sum = 0;
    for (int j = 0; j < 4; j++) {
      sum += hu[i][j];
    }
    win[i] = sum;
    if (i != 0 && mx < win[i]) {
      idx = i;
      mx = win[i];
    }
  }
  cout << idx + 1 << " " << mx;
}
