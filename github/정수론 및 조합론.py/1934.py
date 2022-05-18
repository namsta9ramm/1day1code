test_case=int(input())
ans_list=[]

def math(a,b):
    while b:
        a,b=b,a%b
    return a    

for _ in range(test_case):
    
    a,b=map(int,input().split())
    ans_list.append(a*b//math(a,b))

for j in ans_list:
    print(j)