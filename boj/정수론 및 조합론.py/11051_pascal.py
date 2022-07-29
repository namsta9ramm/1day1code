#동적계획법 알고리즘을 활용한 이항계수법
n,k= map(int,input().split())
ps=[[0] for i in range(1001)]
ps[1].append(1)
for i in range(2,1001):
    for j in range(1,i+1):
        if j==1:
            ps[i].append(1)
        elif j==i:
            ps[i].append(1)
        else:
            ps[i].append(ps[i-1][j-1]+ps[i-1][j])
print(ps[n+1][k+1]%10007)