#회전하는 큐
from collections import deque
a,b=map(int,input().split())
list1=deque([i for i in range(1,a+1)])
list2=list(map(int,input().split()))
#list1=[1,2,3,4,5,6,7,8,9,10]
#   10 1 3 4 5 6 7 8 
# i의 인덱스가 앞과 가까운지 뒤와 가까운지 
# ex) 6 ->index 0 .. 5 ..  9
#list2=[2,9,5]
ans=0
for i in list2:
    while True:
        if list1[0]==i:
         list1.popleft()
         break
        else:
            if list1.index(i)<len(list1)+1-list1.index(i):
                list1.append(list1.popleft())
                ans=ans+1
            else:
                list1.appendleft(list1.pop())
                ans=ans+1
print(ans)