maxlist=[]
for i in range (9):
    a=int(input())
    maxlist.append(a)


big=max(maxlist)
print(big)
print(maxlist.index(big))