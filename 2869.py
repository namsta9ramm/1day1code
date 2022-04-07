#올라가는 달팽이
import sys
import math
a,b,c= map(int,sys.stdin.readline().split())

ans=(c-b)/(a-b)
if type(ans)==int:
    print(ans)
else:
    print(math.ceil(ans))



