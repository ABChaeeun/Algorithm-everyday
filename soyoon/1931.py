n = int(input())
discussion_time = [[0 for j in range(2)] for i in range(n)]

for i in range(n):
    start, end = map(int, input().split())
    discussion_time[i][0] = start
    discussion_time[i][1] = end

print(discussion_time)