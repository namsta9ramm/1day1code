testcase=int(input())
dp=[0]*100
for _ in range(testcase):
    dp[1]=1
    dp[2]=1
    dp[3]=1
    dp[4]=2
    dp[5]=2
    a=int(input())
    for i in range(6,a+1):
        dp[i]=dp[i-3]+dp[i-2]
    print(dp[a])