# import sys
# sys.stdin.read()
copy = []
b = []
while 1:
    a = input()
    if a == ".":
        print("yes")
        break
    else:
        for i in a:
            copy.append(i)
            if ((i == "(") or (i == "[") or (i == ")") or (i == "]")):
                b.append(copy.pop())
                if len(b) >= 2:
                    if (b[-1] == ")") and (b[-2] == "("):
                        b.pop()
                        b.pop()
                    if (b[-1] == "]") and (b[-2] == "["):
                        b.pop()
                        b.pop()
                print(b)
        if len(b) == 0:
            print("yes")
        else:
            print("no")