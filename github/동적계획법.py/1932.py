#정수삼각형
import re


a=int(input())
list1=[]
for i in range(a):
    list1.append(list(map(int,input().split())))
#a=5 i=4
for i in range(1,a):
    for k in range(i+1):
        if k==0:
            list1[i][k]=list1[i-1][0]+list1[i][0]
        elif k==i:
            list1[i][k]=list1[i-1][k-1]+list1[i][k]
        else:
            list1[i][k]=max(list1[i-1][k-1],list1[i-1][k])+list1[i][k]

print(max(list1[-1]))