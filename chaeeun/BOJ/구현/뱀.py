from collections import deque

### 보드의 크기 (N) + 보드 구성
N = int(input())
lst = [[0] * N for _ in range(N)]

### 사과의 개수 (K) + 사과(4)의 위치
K = int(input())
for i in range(K):
    x, y = map(int, input().split())
    lst[x - 1][y - 1] = 4

### 뱀의 방향 변환 횟수 (L) + 뱀의 방향 변환 정보
L = int(input())
dictt = {}
for i in range(L):
    X, C = input().split()
    dictt[int(X)] = C

snake = deque()
snake.append((0, 0))

# 상 우 하 좌
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


##### 함수 정의
def change_dir(dir, C):  # 방향 바꾸는 함수
    if C == "L":  # 왼쪽으로
        dir = (dir - 1) % 4
    else:  # 오른쪽으로
        dir = (dir + 1) % 4
    return dir


##### 뱀은 매 초마다 이동을 하는데 다음과 같은 규칙을 따른다. #####

time = 1
dir = 1
x, y = 0, 0
lst[0][0] = 1

while (True):

    x, y = x + dx[dir], y + dy[dir]

    if 0 <= x < N and 0 <= y < N and lst[x][y] != 1:  # 뱀의 몸이 있는지도 확인

        # 2. 만약 이동한 칸에 사과가 있다면, 그 칸에 있던 사과가 없어지고 꼬리는 움직이지 않는다.
        # if lst[x][y] == 4:
        # lst[x][y] = 0
        # lst[x][y] = 1 # 뱀 +

        # 3. 만약 이동한 칸에 사과가 없다면, 몸길이를 줄여서 꼬리가 위치한 칸을 비워준다. 즉, 몸길이는 변하지 않는다.
        if lst[x][y] == 0:
            lst[snake[0][0]][snake[0][1]] = 0  # 뱀 -
            snake.popleft()

        # 1. 먼저 뱀은 몸길이를 늘려 머리를 다음칸에 위치시킨다.
        snake.append((x, y))
        lst[x][y] = 1
        # print(snake)

        ## 현재 어디 바라보고 있는지 어떻게 알지..? => dir 변수에 저장
        if time in dictt.keys():
            dir = change_dir(dir, dictt[time])

        time += 1


    else:
        # 사과의 위치와 뱀의 이동경로가 주어질 때 이 게임이 몇 초에 끝나는지 계산하라.
        print(time)
        break
