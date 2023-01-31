# 참고 - 아이디어
N = int(input())

times = []
for i in range(N):
    a, b = map(int, input().split())
    times.append([a, b])

times.sort(key = lambda x:(x[1], x[0]))
# x[1] 끝나는 시간이 빠른 회의부터 배정
# x[0] 끝나는 시간이 같다면 시작하는 시간이 빠른 회의부터 배정

T = 0
cnt = 0
for i in range(len(times)):
    if T <= times[i][0] and T <= times[i][1]:
        T = times[i][1]
        cnt += 1

print(cnt)