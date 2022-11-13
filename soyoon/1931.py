import sys

n = int(sys.stdin.readline())

discussion_time = [[0]*2 for i in range(n)]

for i in range(n):
    start, end = map(int, sys.stdin.readline().split())
    discussion_time[i][0] = start
    discussion_time[i][1] = end

discussion_time.sort(key=lambda x:(x[1], x[0]))

end_time = discussion_time[0][1]
cnt = 1

for j in range(1, n):
    if discussion_time[j][0] >= end_time:
        cnt += 1
        end_time = discussion_time[j][1]

print(cnt)