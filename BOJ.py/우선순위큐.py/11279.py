import heapq
ans_list=[]
a=int(input())
dq=[]
for i in range(a): 
    a=int(input())
    if a==0:
        if len(dq)==0:
            ans_list.append(0)
        else:
            ans_list.append(-1*heapq.heappop(dq))
    else:
        heapq.heappush(dq,-a)

for i in ans_list:
    print(i)