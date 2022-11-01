from sys import stdin

N = int(stdin.readline())

queue = []

for i in range(1, N + 1):
    queue.append(i)

while (queue):
    print('{} '.format(queue.pop(0)), end='')  # 맨 위에 있는 카드 버리기
    # print(*queue)

    if not queue:
        break

    queue.append(queue[0])  # 다음에 있는 카드(A)를 제일 아래로 옮기기
    queue.pop(0)  # (A) 삭제
