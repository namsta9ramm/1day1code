#rgb거리

a=int(input())
list1=[]
for i in range(a):
    list1.append(list(map(int,input().split())))
    

for i in range(1,len(list1)):
    list1[i][0]=min(list1[i-1][1],list1[i-1][2])+list1[i][0]
    list1[i][1]=min(list1[i-1][0],list1[i-1][2])+list1[i][1]
    list1[i][2]=min(list1[i-1][0],list1[i-1][1])+list1[i][2]
print(min(list1[-1]))
