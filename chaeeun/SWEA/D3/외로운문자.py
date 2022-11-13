def code():
    T = int(input())
    for tc in range(1, T+1):
        lst = [0]
        strr = input()
        lst[0] = strr[0]
        for i in range(1, len(strr)):
            if strr[i] in lst:
                lst.remove(strr[i])
            else:
                lst.append(strr[i])
        print('#{} '.format(tc), end='')
        lst.sort()
        if len(lst) == 0:
            print('Good')
        else:
            for i in range(len(lst)):
                print(lst[i], sep='', end='')
            print()
 
if __name__ == '__main__':
    code()