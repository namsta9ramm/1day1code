#분해합 생성자 245 198+1+9+8=216
#312342

a=int(input())
num=1
list_ans=[]
while (num<a):
    if sum(map(int, str(num)))+num==a:
        list_ans.append(num)    
    num=num+1

if len(list_ans)==0:
    print(0)
else:
    print(min(list_ans))
    