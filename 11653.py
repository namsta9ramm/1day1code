#소인수분해
n=int(input())
list_ans=[]
#72
while n!=1:
    for i in range(2,n+1):
        if n%i==0:
            list_ans.append(i)
            n=n//i
            break
            
            
for i in list_ans:
    print(i)
