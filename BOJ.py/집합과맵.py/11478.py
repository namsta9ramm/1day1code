#문자열 S가 주어졌을 떄
a=input()
a1=len(a)  #a=ababc /  len a=5
list1=[]
for i in range(1,a1+1):
    for j in range(a1):
        list1.append(a[j:j+i]) # 0,1/1,2/2,3/3,4 0,2/1,3/2,4
        if j+i==a1-1:
            break

k1=set(list1)
print(len(k1))