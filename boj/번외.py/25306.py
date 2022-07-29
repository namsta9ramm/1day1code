a,b,c=map(int,input().split())
list1=[]
for i in range(b):

    list1.append(list(map(int,input().split())))
i=0
for m in list1:
    
    if c in m:
        j=m.index(c)
        o=i
        break
    i=i+1
print(o,j)