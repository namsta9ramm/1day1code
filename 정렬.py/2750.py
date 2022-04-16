#버블정렬을 이용해 정렬하기
a=int(input())
ans_list=[]
for i in range(a):
    j=int(input())
    ans_list.append(j)

for m in range(a-1):
    for n in range(a-1-m):
        if ans_list[n]>ans_list[n+1]:
            ans_list[n],ans_list[n+1]=ans_list[n+1],ans_list[n]

for p in ans_list:
    print(p)

