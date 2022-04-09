#소수 찾기
import sys


import sys
a=int(input())
ans=0
list_1=list(map(int,sys.stdin.readline().split()))

#1 3 5 7
for i in list_1:
    if i==1:
        continue
    else:
        use_num=0
        for j in range(1,i+1):
            if i%j==0:
                use_num=use_num+1
    
    if use_num==2:
        ans=ans+1
print(ans)
