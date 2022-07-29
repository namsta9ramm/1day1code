a=int(input())
list1=list(map(int,input().split()))

def math(a,b):
    while b:
        a,b=b,a%b
    return a    

for i in range(1,a):
    k=math(list1[0],list1[i])
    print(str(list1[0]//k)+"/"+str(list1[i]//k))
