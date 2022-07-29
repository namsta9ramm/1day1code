a,b,c=map(int,input().split())
ans=[]
for i in range(a):
    l=int(input())
    if (b**2+c**2)**(0.5)>=l:
        ans.append('DA')
    else:
        ans.append('NE')

for k in ans:
    print(k)