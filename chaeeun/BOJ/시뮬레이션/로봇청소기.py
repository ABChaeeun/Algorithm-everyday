# 참고

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
r, c, d = map(int, input().split())
lst = []
for i in range(N):
    lst.append(list(map(int, input().split())))
    
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

lst[r][c] = 2
cnt = 1

while True:
    flag = 0
    
    for i in range(4):
        nx = r + dx[(d+3)%4]
        ny = c + dy[(d+3)%4]

        d = (d+3)%4

        if 0 <= nx < N and 0 <= ny < M and lst[nx][ny] == 0: # 전체 직사각형 범위 안
            if lst[nx][ny] == 0:
                lst[nx][ny] = 2
                cnt += 1
                r = nx
                c = ny
                flag = 1
                break # 청소 한 방향이라도 했으면 다음으로 넘어가기

    if flag == 0: # 4 방향 모두 청소가 되어있을때
        if lst[r-dx[d]][c-dy[d]] == 1: # 후진 했는데 벽인 경우
            print(cnt)
            break
        else: # 후진하기
            r, c = r-dx[d], c-dy[d]
            