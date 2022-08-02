#냅색알고리즘
#현재 배낭의 허용 무게보다 넣을 물건의 무게가 더크면 
#넣지 않는다.
#1)현재 넣을 물건의 무게만큼 배낭에서 뺸다.그리고 현재
#물건을 넣는다.
#2)현재 물건을 넣지않고 이전배낭을 가지고 간다
n, k = map(int, input().split())
thing = [[0,0]]
d = [[0]*(k+1) for _ in range(n+1)]
for i in range(n):
    thing.append(list(map(int, input().split())))
for i in range(1, n+1):
    for j in range(1, k+1):
        w = thing[i][0]
        v = thing[i][1]

        if j < w:
            d[i][j] = d[i-1][j]
        else:
            d[i][j] = max(d[i-1][j], d[i-1][j-w]+v)
print(d[n][k])
