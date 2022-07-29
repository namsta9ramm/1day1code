# 15651
n,m = list(map(int,input().split())) # n=3,m=2
s = []
def dfs():
    if len(s)==m:
        print(' '.join(map(str,s)))
        return
    
    for i in range(1,n+1):
        
            s.append(i)
            dfs()
            s.pop()

dfs()