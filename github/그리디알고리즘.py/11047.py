a,b=map(int,input().split())
as_list=[]
for i in range(a):
    as_list.append(int(input()))
ans_list=[]
sum=0
while True:
    for j in as_list:
        if b//j!=0:
            ans_list.append(b//j)
    if len(ans_list)==0:
        break
    as_list=ans_list
    sum=sum+min(ans_list)

print(sum)