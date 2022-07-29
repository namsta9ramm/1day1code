def factorial(n):
    if n==1 or n==0:
        return 1
    else:
        return n*factorial(n-1)
    

test_case=int(input())
ans_list=[]
for _ in range(test_case):
    a,b=map(int,input().split())
    ans_list.append(factorial(b)//(factorial(b-a)*factorial(a)))

for j in ans_list:
    print(j)