a=int(input())
dp=[0]*(301)
list_stair=[0]*(301)
#dp=[0,10,30,15+,0,0,0]
#dp[3]=stair[2]+max(dp[1],stair[2])
#stair=[10,20,15,25,10,20]

for i in range(a):
    list_stair[i]=int(input())

dp[0]=list_stair[0]
dp[1]=list_stair[1]+list_stair[0]
dp[2]=list_stair[2]+max(list_stair[1],list_stair[0])

for i in range(3,a+1):
    dp[i]=list_stair[i]+max(dp[i-2],list_stair[i-1]+dp[i-3])
    
print(dp[a-1])