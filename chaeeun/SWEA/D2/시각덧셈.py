T = int(input())

for tc in range(1, T+1):
    h1, m1, h2, m2 = map(int, input().split())

    h_sum = h1 + h2
    m_sum = m1 + m2

    if h_sum > 12:
        h_sum = h_sum - 12
    if m_sum > 60:
        m_sum = m_sum - 60
        h_sum += 1

    print('#{} {} {}'.format(tc, h_sum, m_sum))