#소트인사이드

from audioop import reverse


a=input()
list_1=[]
for j in a:
    list_1.append(int(j))

list_1.sort(reverse=True)

for k in list_1:
    print(k,end="")
