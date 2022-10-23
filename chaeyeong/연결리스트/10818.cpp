#include <iostream>
using namespace std;

int main() {
  int n;cin>>n;
	int mx=-1e9;
  int mn=1e9;
	for(int i=0;i<n;i++){
		int tmp;cin>>tmp;
		mx=max(mx,tmp);
		mn=min(mn,tmp);
	}
	cout<<mn<<" "<<mx<<endl;
}
