import sys
input = sys.stdin.readline

lst = [int(input()) for _ in range(9)]

max_num = max(lst)
print(max_num)
print(lst.index(max_num)+1)