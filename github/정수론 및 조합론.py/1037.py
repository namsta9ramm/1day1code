#약수 
a=int(input())
list1=list(map(int,input().split()))

if a==1:
    print(list1[0]**2)
else:
    print(min(list1)*max(list1))