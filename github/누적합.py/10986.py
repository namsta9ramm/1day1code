# 1,2 2,3 3,1 1,2 
a,b=map(int,input().split())
list1=list(map(int,input().split()))
k=0
ans=0
for i in range(a): # i=0 (1,a)
    for j in range(i+1,a+1):
        k=sum(list1[i:j])
        
        if k%3==0:
            ans=ans+1
           

print(ans)