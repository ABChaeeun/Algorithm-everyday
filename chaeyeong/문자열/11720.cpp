#include <iostream>
using namespace std;

string num;
int size;
int sum = 0;

int main() {
  cin >> size;
  cin >> num;
  for(int i=0; i<size; i++) {
    sum += num[i] - 48;
  }
  cout << sum;
}
