import sys
a=int(input())
list_1=[]
for i in range(a):
    [x,y]=map(int,input().split())
    list_1.append([x,y])
ans_list=sorted(list_1)

for k in range(a):
    print(ans_list[k][0],ans_list[k][1])
    
    

