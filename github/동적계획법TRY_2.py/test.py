def fibonachi(n):
    
    f=[0]*(n+1)
    f[1]=1
    f[2]=1
    for i in range(3,n+1):
        f[n]=f[n-1]+f[n-2]
        
fibonachi(5)