def num(k):
    if k==1:
        return False
    else:
        for j in range(2,(k**(0.5)+1)):
            
            if k%j==0:
                return False
        return True 
shit_list=list(range(2,246912))
ans_list=[]
for i in shit_list:
    if num(i):
        ans_list.append(i)

while True:
    n=int(input())
    if n==0:
        break
    ans=0
    for i in ans_list:
        if n<i<=2*n:
            ans=ans+1
    print(ans)