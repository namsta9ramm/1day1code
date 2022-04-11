#골드바흐의 추측 
#2보다 큰 모든 짝수는 두 소수의 합으로 표현가능
test_case=int(input())

def num(n):
    if n==1:
        return False
    else:
        for i in range(2,int(n**(0.5)+1)):
            if n%i==0:
                return False
        return True

num_list=list(range(2,10000))
ans_list=[]
for i in num_list:
    if num(i):
        ans_list.append(i)

for i in range(test_case):
    a=int(input())
    b=a//2
    c=b
    for _ in range(10000):
        if c in ans_list and b in ans_list:
            print(b,c)
            break
        b=b-1
        c=c+1
