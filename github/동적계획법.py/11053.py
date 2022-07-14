#참조 
n = int(input())
a = list(map(int, input().split()))
dp = [0 for i in range(n)]
#dp=[0,1,1,2,0]
#n=6 i=0 , i=1 j=0 ,i=2 j=0, i=3 j=1  
for i in range(n):
    for j in range(i):
        if a[j]<a[i] and dp[i] < dp[j]:
            dp[i] = dp[j]
        
    dp[i] += 1

print(max(dp))