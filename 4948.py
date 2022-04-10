def num(k):
    if k==1:
        return False
    else:
        for j in range(2,(int(k**(0.5))+1)):
            
            if k%j==0:
                return False
        return True 

new_list=list(range(2,246912))
ans_list=[]
for i in new_list:
    if num(i):
        ans_list.append(i)

while True:
   
    n=int(input())
    if n==0:
        break
    cnt=0
    for i in ans_list:
        if n<i<=n*2:
            cnt=cnt+1
    print(cnt)