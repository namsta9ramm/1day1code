a,b=map(int,input().split())
list1=list(map(int,input().split()))
ans_list=[0]
k=0
for i in list1:
    k=k+i
    ans_list.append(k)
    #ans_list=[0,5,9,12]
final_list=[]
for _ in range(b):
    x,y=map(int,input().split())
    final_list.append(ans_list[y]-ans_list[x-1])
for k in final_list:
    print(k)
