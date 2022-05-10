import sys
a=int(input())
list_1=[]
z=0
for i in range(a):
    x,y=input().split()
    num_x=int(x)
    list_1.append([num_x,z,y])
    z=z+1
ans_list=sorted(list_1)

for k in range(a):
    print(ans_list[k][0],ans_list[k][2])

    