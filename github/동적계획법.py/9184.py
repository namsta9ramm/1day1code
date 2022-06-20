def w(a,b,c):

    if a<=0 or b<=0 or c<=0:
        return 1
    if a > 20 or b > 20 or c > 20:
        return w(20, 20, 20)
    if dp[a][b][c]:
        return dp[a][b][c]
    if a < b and b < c: 
        dp[a][b][c]=w(a, b, c-1) + w(a, b-1, c-1) - w(a, b-1, c)
        return dp[a][b][c]
    
    dp[a][b][c]= w(a-1, b, c) + w(a-1, b-1, c) + w(a-1, b, c-1) - w(a-1, b-1, c-1)
    return dp[a][b][c]
dp=[[[0]*21 for _ in range(21)] for _ in range(21)]

a,b,c=map(int,input().split())
while (a!=-1 or b!=-1 or c!=-1):
    print('w({0}, {1}, {2}) = {3}'.format(a,b,c,w(a,b,c)))
    a,b,c=map(int,input().split())