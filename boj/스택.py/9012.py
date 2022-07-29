a=int(input())
ans_list=[]
for i in range(a):
    list_1=[0]*50
    k=input()
    for j in k:
        if j=='(':
            list_1.append('1')
        else:
            list_1.pop()
    
    if '1' not in list_1 and len(list_1)==50:
        ans_list.append("YES")
    else:
        ans_list.append("NO")
for m in ans_list:
    print(m)