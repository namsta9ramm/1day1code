#그룹단어체커
a=int(input())
sum=0
for i in range(a):
    #b='happyh'
    
    #b='happy'
    b=input()
    list_b=list(b)
    #list_b=['h','a','p','p','y']
    ans=[]
    j=0
    for p in list_b:
        
        
        ans.append(list_b.index(p))
    #ans=[0,1,2,2,4] k=0,1,2,3
    for k in range(len(ans)-1):
        if ans[k]<=ans[k+1]:
            j=j+1
    
    if j==len(ans)-1:
        sum=sum+1
    
print(sum)

