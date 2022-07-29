a=int(input())
list1=list(map(int,input().split()))
dp=[0]*(a)
#a=10 , dp [10,6,9,10,15,21,0,0,0,0]
dp[0]=list1[0]
for i in range(1,a):
    dp[i]=max(dp[i-1]+list1[i],list1[i])
print(dp)
print(max(dp))