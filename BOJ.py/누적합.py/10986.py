import sys
total, tar = map(int,sys.stdin.readline().split())
tem = list(map(int,sys.stdin.readline().split()))
#tem=[1,2,3,1,2]
# 부분합 0 1 2
# list1=[2,2,2]
list1= [0 for i in range(tar)]
presum = 0
list1[0] = 1
for i in range(total):
    presum=presum+tem[i]

    list1[presum%tar] += 1
    print(list1)
ans=0
for i in list1:

    ans += i*(i-1)//2

print(ans)