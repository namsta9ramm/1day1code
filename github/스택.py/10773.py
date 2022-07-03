a=int(input())
list_ans=[]
for i in range(a):
    k=int(input())
    if k==0:
        list_ans.pop()
    else:
        list_ans.append(k)

print(sum(list_ans))