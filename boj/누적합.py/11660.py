a,b=map(int,input().split())
list1=[]
for _ in range(a):
    list1.append(list(map(int,input().split())))
dp=[[0 for i in range(a+1)] for i in range(a+1)]

for i in range(a): 
    for j in range(a):
        dp[i+1][j+1]=list1[i][j]+dp[i][j+1]+dp[i+1][j]-dp[i][j]
ans=0
ans_list=[]
for _ in range(b):
    x,y,z,p=map(int,input().split())
    ans_list.append(dp[z][p]-dp[z][y-1]-dp[x-1][p]+dp[x-1][y-1])

for q in ans_list:
    print(q)