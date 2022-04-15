import sys
data = []
n = int(sys.stdin.readline())
for i in range(n):
    data.append(list(map(int,sys.stdin.readline().split())))

for j in range(n):
    rank=1
    for k in range(n):
        if data[j][0]<data[k][0] and data[j][1]<data[k][1]:
           rank=rank+1 
    print(rank,end=" ")