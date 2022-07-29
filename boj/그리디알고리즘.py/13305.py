a=int(input())
list_distance=list(map(int,input().split()))
list_price=list(map(int,input().split()))

sum1=list_distance[0]*list_price[0]
del list_distance[0]
del list_price[-1]
del list_price[0]
while True:
    a=list_price.index(min(list_price))
    ans=min(list_price)*sum(list_distance[a::])
    sum1=sum1+ans
    del list_price[a::]
    del list_distance[a::]
    if len(list_distance)==0:
        break
print(sum1)



#ans=list_distacne[0]