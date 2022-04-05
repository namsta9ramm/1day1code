# self number 
def d(n):
    num1=[int (i) for i in str(n) ]
    num=n+sum(num1)
    return num

k=1
fake_list=[]
real_list=[]
while k<10000:
    fake_list.append(d(k))
    real_list.append(k)
    k=k+1
    

fake2_list=[]
for value in fake_list:
    if value not in fake2_list:
        fake2_list.append(value)

me=set(real_list)-set(fake2_list)
final_list=list(me)
final_list.sort()




for i in final_list:
    print(i)

