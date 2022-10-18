#include <iostream>
using namespace std;

char phone_List[10000][11];
struct TRIE
{
	bool Finish;
	TRIE *Node[10];
	TRIE()
	{
		Finish = false;
		for (int i = 0; i < 10; i++)
		{
			Node[i] = NULL;
		}
	}
	void insert(char *str)
	{
		if (*str == '\0')
		{
			Finish = true;
			return;
		}
		int Cur = *str - '0';
		if (Node[Cur] == NULL)
			Node[Cur] = new TRIE();
		Node[Cur]->insert(str + 1);
	}
	bool find(char *str)
	{
		if (*str == '\0')
		{
			return false;
		}
		if (Finish == true)
			return true;

		int Cur = *str - '0';
		if (Node[Cur] == NULL)
			return false;
		return Node[Cur]->find(str + 1);
	}
};

int main() {
  int t, n;
	cin >> t;
	while (t--)
	{
		cin >> n;
		TRIE *Root = new TRIE();
		for (int i = 0; i < n; i++)
		{
			cin >> phone_List[i];
			Root->insert(phone_List[i]);
		}
		bool tof = false;
		for (int i = 0; i < n; i++)
		{
			if (Root->find(phone_List[i]))
			{
				tof = true;
				break;
			}
		}
		if (tof == false)
			cout << "YES" << endl;
		else
			cout << "NO" << endl;
	}
}
