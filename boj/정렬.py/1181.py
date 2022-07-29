#단어 길이 순서대로 정렬
from os import remove
import sys
a=int(input())
list_1=[]
for i in range(a):
    x=input()
    x1=len(x)
    list_1.append([x1,x])
ans_list=sorted(list_1)
ans_list1=list(set(map(tuple,ans_list)))
ans_list1=sorted(ans_list1)
for k in range(len(ans_list1)):
    
    print(ans_list1[k][1])

    
