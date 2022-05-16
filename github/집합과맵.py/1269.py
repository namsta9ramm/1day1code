#대칭차집합
import sys

_,_=map(int,input().split())
list1=list(map(int,input().split()))
list2=list(map(int,input().split()))
t1=set(list1)
t2=set(list2)
ans=(t1-t2)|(t2-t1)
ans_list=list(ans)
print(len(ans_list))
