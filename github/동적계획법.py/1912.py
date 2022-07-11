a=int(input())
list1=list(map(int,input().split()))
ans_list=[0]*a
ans_list[0]=list1[0]
for i in range(a):
    ans_list[i]=max(ans_list[i-1]+list1[i],list1[i])
print(max(ans_list))
#10
#10 -4 3 1 5 6 -35 12 21 -1
#ans_list=[10,6,9,10,15,21,-14,]