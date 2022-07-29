ans_list=[]
while True:
    a,b=map(int,input().split())
    if a<b:
        if b%a==0:
            ans_list.append("factor")
        else:
            ans_list.append("neither")
    
    elif a==0 and b==0:
        break
    
    
    
    else:
        if a%b==0:
            ans_list.append("multiple")
        else:
            ans_list.append("neither")
for i in ans_list:
    print(i)
        