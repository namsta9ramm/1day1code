#포도주시식
a=int(input())
list1=[0]
for i in range(a):
    list1.append(int(input()))
#list1=[0,6,10,13,9,8,1] a=6
# range(6): 
#max=[0,6,16]
max_list=[0]
max_list.append(list1[1])
if a>1:
    max_list.append(list1[1]+list1[2])
# i=3 0 10 13 , i=4 , i=7   max[4]+list[6]+list[7],max[5]+list[7],max[6] 

for i in range(3,a+1):# i=4  
    max_list.append(max(max_list[i-3]+list1[i-1]+list1[i],max_list[i-2]+list1[i],max_list[i-1]))
print(max_list[a])