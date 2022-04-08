# ACM 호텔 걷는 거리가 짧도록 방을 배정
import sys
test_case=int(input())
list1=[]
# h=2 w=4 n=2(201), 6(203), 8(204)
for i in range(test_case):
    h,w,n=map(int,sys.stdin.readline().split())
    if (n%h==0):
        ho=n//h
        floor=h

    else:
         ho=n//h+1
         floor=n%h
    room_num=str(floor)+str(ho).zfill(2)
    list1.append(room_num)

for k in list1:
    print(k)
# n//h+1:호수 n%h:층수 
 