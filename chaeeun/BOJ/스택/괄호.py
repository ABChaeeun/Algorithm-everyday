T = int(input())

for tc in range(T):
    stack = []
    lst = input()

    for i in range(len(lst)):
        if lst[i] == '(':
            stack.append('(')
        else:
            if len(stack) == 0:
                stack.append(')')
                break
            else:
                stack.pop()

    # print(*stack)
    if stack:
        print("NO")
    else:
        print("YES")
