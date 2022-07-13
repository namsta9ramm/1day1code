#포도주시식

a=int(input())
list1=[0]
for i in range(a):
    list1.append(int(input()))
#list1=[0,6,10,13,9,8,1] a=6
# range(6): 
max_list=[0]
max_list.append(list1[1])
max_list.append(list1[1]+list1[2])

for i in range(3,a+1):
    max_list.append(max(max_list[i-3]+list1[i-1]+list1[i],max_list[i-2]+list1[i],max_list[i-1]))
print(max_list[a])