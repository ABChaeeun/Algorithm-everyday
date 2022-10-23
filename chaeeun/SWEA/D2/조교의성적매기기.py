T = int(input())

for tc in range(1, T+1):
    
    N, K = map(int, input().split())

    sums = []
    for n in range(1, N+1):
        mid, final, assignment = map(int, input().split())
        sum = (mid*0.35) + (final*0.45) + (assignment*0.2)
        sums.append([sum, n])

    sums.sort(reverse = True)

    n_same = N/10
    for i in range(N):
        if i // n_same == 0:
            sums[i].append('A+')
        elif i // n_same == 1:
            sums[i].append('A0')
        elif i // n_same == 2:
            sums[i].append('A-')
        elif i // n_same == 3:
            sums[i].append('B+')
        elif i // n_same == 4:
            sums[i].append('B0')
        elif i // n_same == 5:
            sums[i].append('B-')
        elif i // n_same == 6:
            sums[i].append('C+')
        elif i // n_same == 7:
            sums[i].append('C0')
        elif i // n_same == 8:
            sums[i].append('C-')
        elif i // n_same == 9:
            sums[i].append('D0')
            
    for nn in range(N):
        if sums[nn][1] == K:
            print("#{}".format(tc), sums[nn][2])