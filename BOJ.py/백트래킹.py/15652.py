# 15652
n,m = list(map(int,input().split())) # n=3,m=2
s = []
def dfs(start):
    if len(s)==m:
        print(' '.join(map(str,s)))
        return
    
    for i in range(start,n+1):
        
            s.append(i)
            dfs(i)
            s.pop()

dfs(1)