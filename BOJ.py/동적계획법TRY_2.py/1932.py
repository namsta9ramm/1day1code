a=int(input())

list1=[]
for i in range(a):
    list1.append(list(map(int,input().split())))

for i in range(1,a):
    for j in range(len(list1[i])):
        if j==0:
            list1[i][j]=list1[i][j]+list1[i-1][j]
        elif j==len(list1[i])-1:
            list1[i][j]=list1[i][j]+list1[i-1][-1]
        else:
            list1[i][j]=list1[i][j]+max(list1[i-1][j-1],list1[i-1][j])

print(max(list1[-1]))

