T = int(input())

def div(alph, num, k):
    if num % k == 0:
        alph += 1
        return div(alph, num//k, k)
    else:
        return alph

for tc in range(1, T+1):

    num = int(input())
    
    a = 0; b = 0; c = 0; d = 0; e = 0
    a = div(a, num, 2)
    b = div(b, num, 3)
    c = div(c, num, 5)
    d = div(d, num, 7)
    e = div(e, num, 11)

    print('#{} '.format(tc), end='')
    print(a, b, c, d, e)