a=int(input())
b=int(input())
c=int(input())

cal=a*b*c
list1=[]
cal1=str(cal)
for i in range(len(cal1)):
    list1.append(int(cal1[i]))

for k in range(10):
    print(list1.count(k))


