a=int(input())
list1=[]
for i in range(a):
    list1.append(list(map(int,input().split())))

list1.sort(key=lambda x:x[0])

list1.sort(key=lambda x:x[1])
cnt=1
for i in range(1,a):
    if list1[i][0]>=list1[i-1][1]:
        
        cnt=cnt+1
        
    else:
        list1[i][0]=list1[i-1][0]
        list1[i][1]=list1[i-1][1]

print(cnt)