#평면상의 외적 외적값이 > 0 - >반시계 외적값 <0 -> 시계
x1,y1=map(int,input().split())
x2,y2=map(int,input().split())
x3,y3=map(int,input().split())

ax=x1-x2
ay=y1-y2

bx=x3-x2
by=y3-y2
if ax*by-ay*bx>0:
    print(-1)
elif ax*by-ay*bx<0:
    print(1)
else:
    print(0)


