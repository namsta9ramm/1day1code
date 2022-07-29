#듣보잡
#듣도 못한 사람 N 보도 못한 사람의 수 M 
import sys
a,b=map(int,input().split())

see_not=[]
hear_not=[]

for i in range(a):
    see_not.append(input())

for j in range(b):
    hear_not.append(input())

intersection = list(set(hear_not) & set(see_not))
print(len(intersection))
intersection_ans=sorted(intersection)
for k in intersection_ans:
    print(k)