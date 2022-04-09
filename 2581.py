import sys
a=int(input())
b=int(input())
ans_list=[]
for i in range(a,b+1):
    use_num=0
    for j in range(1,i+1):
            if i%j==0:
                use_num=use_num+1
    
    if use_num==2:
        ans_list.append(i)

if len(ans_list)==0:
    print("-1")
else:
    print(sum(ans_list))
    print(min(ans_list))
