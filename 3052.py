list_1=[]

for i in range(10):
    a=int(input())
    list_1.append(a%42)
#case1 [1,2,3,4,5,6,7,8,9,10]
#case2 [0,0,0,0,0,0,0,0,0,0]
#case3 [1,1,2,2,3,3,4,4,5,5]

result=[]

for i in list_1:
    if i not in result:
        result.append(i)

print(len(result))

