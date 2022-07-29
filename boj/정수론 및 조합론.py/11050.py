a,b=map(int,input().split())
list1=[]
list2=[]
for i in range(a,0,-1):
    list1.append(i)

for j in range(b,0,-1):
    list2.append(j)
ans1=1
ans2=1
for k in range(b):
    ans1=ans1*list1[k]
for m in range(b):
    ans2=ans2*list2[m]

print(ans1//ans2)