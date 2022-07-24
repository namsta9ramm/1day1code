a=int(input())
list1=list(map(int,input().split()))
ans_list=[]
for i in range(a):
    used_list=[]
    
    for k in range(i+1,a):
        if list1[i]<list1[k]:
            used_list.append(list1[k])
    used_list=sorted(used_list)
    if len(used_list)==0:
        ans_list.append(-1)

    else:
        ans_list.append(used_list[0])

print(*ans_list)