def dfs(x):
    if len(s) == m:
        print(' '.join(map(str, s)))
        return
    for i in range(x+1, n+1):
        if visited[i]:
            continue
        visited[i] = True
        s.append(i)
        dfs(i)
        s.pop()
        
       
        visited[i] = False
            

n, m = map(int, input().split())
s = []
visited = [False] * (n+1)

dfs(0)