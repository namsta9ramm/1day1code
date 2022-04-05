#문자열 반복
a,b=input().split()
list_ans=[str(i) for i in b]
print_ans=[]
for i in list_ans:
    print_ans.append(int(a)*i)

for k in print_ans:
    print(k,end="")

