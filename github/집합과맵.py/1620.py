a,b=map(int,input().split())
dict_1={}
dict_2={}
list_2=[]
for j in range(a):
    m=input()
    dict_1[j]=m
    dict_2[m]=j
for k in range(b):
    list_2.append(input())

for i in list_2:
    if i.isdigit()==True:
        i1=int(i)
        print(dict_1[i1-1])
    else:
        print(dict_2[i]+1)
