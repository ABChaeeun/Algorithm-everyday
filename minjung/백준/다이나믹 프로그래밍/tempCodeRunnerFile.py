for i in range(n):
        for j in range(n):
            if i == j:
                dp[i][i] = novel[i]
            if j == i+1:
                dp[i][i+1]= novel[i]+novel[i+1]
    