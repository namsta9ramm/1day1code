#영수증
cost=int(input())
anssum=0
case=int(input())
for i in range(case):
    a,b=map(int,input().split())
    anssum=anssum+a*b

if anssum==cost:
    print("Yes")
else:
    print("No")