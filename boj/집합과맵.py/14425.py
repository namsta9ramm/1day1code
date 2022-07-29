a,b=map(int,input().split())
list1=[]
list2=[]
for i in range(a):
    list1.append(input())
for j in range(b):
    list2.append(input())

ans=0

for k in range(b):
    if list2[k] in set(list1):
        ans=ans+1

print(ans)