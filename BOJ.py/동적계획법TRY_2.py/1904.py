#n=1 1
#n=2 2
#n=3 3
dp=[0]*1000000
dp[1]=1
dp[2]=2
a=int(input())

for i in range(3,a+1):
    dp[i]=(dp[i-1]+dp[i-2])%15746
print(dp[a])
