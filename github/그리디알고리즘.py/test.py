a=int(input())
list_distance=list(map(int,input().split()))
list_price=list(map(int,input().split()))

sum=list_distance[0]*list_price[0]
a=list_price.index(min(list_price))
ans=min(list_price)*sum(list_distance[a::])    
print(ans)
