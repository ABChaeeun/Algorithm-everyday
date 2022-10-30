from sys import stdin

# N = int(input())
N = int(stdin.readline())

stack = []

for tc in range(N):
    # cmd = input().split()
    cmd = stdin.readline().split()

    # stack = [] # 밖에서 선언 해줘야 함!!

    if cmd[0] == 'push':
        stack.append(cmd[1])

    elif cmd[0] == 'pop':
        if stack:
            print(stack[-1])
            del stack[-1]
        else:
            print(-1)

    elif cmd[0] == 'size':
        print(len(stack))

    elif cmd[0] == 'empty':
        if stack:
            print(0)
        else:
            print(1)

    elif cmd[0] == 'top':
        if stack:
            print(stack[-1])
        else:
            print(-1)
