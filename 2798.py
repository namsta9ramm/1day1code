#블랙잭 브루토포스
import sys


a,b=map(int,sys.stdin.readline().split())
data = list(map(int,sys.stdin.readline().split()))
ans_data=[]
for i in range(a):
    for j in range(1,a):
        for k in range(2,a):
            if b>=data[i]+data[j]+data[k] and i!=j and j!=k and k!=i:
            
                
                ans_data.append(data[i]+data[j]+data[k])

print(max(ans_data))
