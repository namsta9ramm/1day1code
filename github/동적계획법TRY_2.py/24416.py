def fib(n):
    
    if n==1 or n==2:
        return 1
    else:
        return fib(n-1)+fib(n-2)
    

def fibonachi(n):
    
    f=[0]*(n+1)
    f[1]=1
    f[2]=1
    for i in range(3,n+1):
        f[n]=f[n-1]+f[n-2]
    
    return f[n]
    

a=int(input())
print(fib(a),fibonachi(a))
