T = int(input())

for tc in range(1, T+1):
    won = int(input())

    a = won // 50000
    if a != 0:
        won -= a*50000
        
    b = won // 10000
    if b != 0:
        won -= b*10000
        
    c = won // 5000
    if c != 0:
        won -= c*5000
        
    d = won // 1000
    if d != 0:
        won -= d*1000
        
    e = won // 500
    if e != 0:
        won -= e*500
        
    f = won // 100
    if f != 0:
        won -= f*100
        
    g = won // 50
    if g != 0:
        won -= g*50
        
    h = won // 10
    if h != 0:
        won -= h*10

    print('#{}'.format(tc))
    print(a, b, c, d, e, f, g, h)