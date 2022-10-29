from sys import stdin

# N = int(input())
N = int(stdin.readline())

queue = []

for tc in range(N):
    
    # cmd = input().split()
    cmd = stdin.readline().split()
    if cmd[0] == 'push':
        queue.append(cmd[1])
    elif cmd[0] == 'pop':
        if queue:
            print(queue[0])
            del queue[0]
        else:
            print(-1)
    elif cmd[0] == 'size':
        print(len(queue))
    elif cmd[0] == 'empty':
        if queue:
            print(0)
        else:
            print(1)
    elif cmd[0] == 'front':
        if queue:
            print(queue[0])
        else:
            print(-1)
    elif cmd[0] == 'back':
        if queue:
            print(queue[-1])
        else:
            print(-1)
