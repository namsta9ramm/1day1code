n=int(input())
list1=[0]*(n+1)

for i in range(2,n+1):
    
    list1[i]=list1[i-1]+1
    if i %2==0:
        list1[i]=min(list1[i],list1[i//2]+1)
    if i %3==0:
        list1[i]=min(list1[i],list1[i//3]+1)
print(list1[n])
#list1[2]=1
#n=2 ->1
#n=3  - >  1 
#n=4 -> 2
#n=5 -> 3
#n=6 ->2 
#n=7 ->3
#n=8 ->3
#n=9 ->2
#n=10 ->3
#n=11 ->4
#n=12 ->3   n=17 