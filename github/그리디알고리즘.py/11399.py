a=int(input())
list1=list(map(int,input().split()))
list1=sorted(list1)
new_list=[]
new_list.append(list1[0])
for i in range(1,len(list1)):
    new_list.append(list1[i]+new_list[i-1])

print(sum(new_list))