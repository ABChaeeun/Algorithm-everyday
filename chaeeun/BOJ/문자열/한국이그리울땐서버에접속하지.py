import sys
input = sys.stdin.readline

N = int(input())
p = input().strip()
pattern = p.split('*')


def check(strr): 
    if len(strr) >= len(p) - 1:
        if pattern[0] == strr[0:len(pattern[0])] and pattern[1] == strr[len(strr)-len(pattern[1]):len(strr)]:
            return 'DA'
        else:
            return 'NE'
    else:
        return 'NE'

lst = []
for _ in range(N):
    lst.append(input().strip())

for i in range(N):
    print(check(lst[i]))