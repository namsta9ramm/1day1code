import sys
read=sys.stdin.readline
word1,word2=read().strip(),read().strip()
a=len(word1)
b=len(word2)
dp=[[0]*(a+1) for _ in range(b+1)]
for i in range(1,a+1):
    for j in range(1,b+1):
        if word1[i-1]==word2[j-1]:
            dp[i][j]=dp[i-1][j-1]+1
        else:
             dp[i][j]=max(dp[i-1][j],dp[i][j-1])

print(dp[-1][-1])