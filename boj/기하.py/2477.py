k=int(input())

list1=[]
for _ in range (6):
    [a,b]=map(int,input().split())
    list1.append([a,b])
max_low=0
max_col=0
index_1=0
index_2=0
for i in range(6):
    if list1[i][0]== 1 or list1[i][0]==2: 
        if max_low<list1[i][1]:
            max_low=list1[i][1]
            index_1=i
    else:
        if max_col<list1[i][1]:
            max_col=list1[i][1]
            index_2=i
min_col=abs((list1[(index_1-1)%6][1])-list1[(index_1+1)%6][1])
min_row=abs((list1[(index_2-1)%6][1])-list1[(index_2+1)%6][1])

print(k*(max_low*max_col-min_col*min_row))
