a,b=map(int,input().split())
list_1=list(map(int,input().split()))
list_2=[]
ans=sum(list_1[:b])
list_2.append(ans)
for i in range(1,a-b+1): #a=10, b=2 range(1,9)->8
    ans=ans-list_1[i-1]+list_1[i+b-1]
    list_2.append(ans)
print(max(list_2))
