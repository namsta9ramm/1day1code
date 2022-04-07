# 1 ->6 ->12->
# 위 :2 6 10 14 18   양 사이드 :4 6 8 10
# 4n-2 , 2+2n


i=1
n=int(input())

while 3*i*i-3*i+2<n:
    i=i+1

print(i)

