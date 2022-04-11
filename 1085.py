import sys

a,b,c,d=map(int,sys.stdin.readline().split())

num_1=a
num_2=b
num_3=d-b
num_4=c-a
ans_list=[num_1,num_2,num_3,num_4]
print(min(ans_list))