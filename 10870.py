def fibonacci(n):
    sum=0
    if n==0:
        return 0
    elif n==1:
        return 1
    
    elif n>=2:
        return fibonacci(n-1)+fibonacci(n-2)
n=int(input())
print(fibonacci(n))
