#동적계획법 알고리즘을 활용한 이항계수법
import math

a,b=map(int,input().split())
m=math.factorial(a)//(math.factorial(a-b)*math.factorial(b))
print(m%10007)
