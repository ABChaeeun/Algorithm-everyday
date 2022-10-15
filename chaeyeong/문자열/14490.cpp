#include <iostream>
#include <string>

using namespace std;

typedef long long i64;
inline i64 gcd(i64 a, i64 b) { if (a % b == 0)return b; else { return gcd(b, a % b); } }

int main() {
  string str;
  int idx;
  cin >> str;

  for(int i = 0; i<str.length(); i++) {
    if(str[i] == ':') {
      idx = i;
    }
    }
  int a = stoi(str.substr(0, idx));
  int b = stoi(str.substr(idx+1, str.length()-idx));

  int divide = gcd(a, b);

  cout << a/divide << ':' << b/divide;
}
