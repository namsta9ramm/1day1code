#숫자카드
import sys
a=int(input())
list1=set(map(int,input().split()))
a2=int(input())
list2=list(map(int,input().split()))
for i in range(a2):
    if list2[i] in list1:
        list2[i]=1
    else:
        list2[i]=0


print(*list2)