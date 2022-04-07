#매년 임대로 재산세 보험료 금여 . .A만원 고정비용
#한대의 노트북 재료비, 인건비 B만원 가변비용
#A=1000,B=70 
import sys

a,b,c=map(int, sys.stdin.readline().split())

if (c-b)<=0:
    print(-1)
else:
    print((a//(c-b))+1)

  