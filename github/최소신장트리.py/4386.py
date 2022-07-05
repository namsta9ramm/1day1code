import math
import sys
#별자리 만들기
#첫번쨰 줄에 별의 개수 n이 주어진다
def find_parent(x):
    if parent[x] != x:
        parent[x] = find_parent(parent[x])
    return parent[x]

def union_parent(a, b):
    a = find_parent(a)
    b = find_parent(b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b
n=int(input())
parent=[i for i in range(n+1)]
stars = []
total_cost = 0
edges=[]
for _ in range(n):
    a, b= map(float, input().split())    
    stars.append((a, b))
for i in range(n-1): #v=3  m=0 , range(1,3) [[1,2],[2,3],[3,4]]
    for j in range(i+1,n):
        edges.append((math.sqrt((stars[i][0]-stars[j][0])**2+(stars[i][1]-stars[j][1])**2),i,j))
edges.sort()

for k in range(n):
    cost, a, b = edges[k]
   
    if find_parent(a) != find_parent(b):
        union_parent(a, b)
        total_cost += cost

print(round(total_cost,2))