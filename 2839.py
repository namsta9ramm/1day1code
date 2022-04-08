#설탕 공장 3kg 5kg 짜리 봉지 ex) 18kg 5->3 3->1
# 11 3 3 5    30 6 0 / 3 5 / 0 10 
# 3 5 8
arr=[0 for i in range(50000)]
for i in range(0,1001):
    
    for j in range(0,1667):
        
        
        if 3*j+5*i<=5000:
            if arr[3*j+5*i]==0:
                arr[3*j+5*i]=i+j
            else:
              arr[3*j+5*i]=min(arr[3*j+5*i],i+j)
        else:
            continue
        
    
x=int(input())
if arr[x]==0:
    print("-1")
else:
    print(arr[x])