lst = ['a','e','i','o','u']

def test(strr):
    # 모음(a,e,i,o,u) 하나를 반드시 포함하여야 한다.
    cnt = 0
    for i in lst:
        if i in strr:
            cnt += 1
    if cnt == 0:
        return False

    # 모음이 3개 혹은 자음이 3개 연속으로 오면 안 된다.
    for i in range(len(strr)-2):
        if strr[i] in lst:
            if strr[i+1] in lst:
                if strr[i+2] in lst:
                    return False
        if strr[i] not in lst:
            if strr[i+1] not in lst:
                if strr[i+2] not in lst:
                    return False
                    
    # 같은 글자가 연속적으로 두번 오면 안되나, ee 와 oo는 허용한다.
    for i in range(len(strr)-1):
        if strr[i] == strr[i+1]:
            if strr[i] != 'e' and strr[i] != 'o':
                return False
    
    
    return True


while True:
    strr = input()
    
    if strr == 'end':
        break
        
    if test(strr):
        print('<%s> is acceptable.' % (strr))
    else:
        print('<%s> is not acceptable.' % (strr))
