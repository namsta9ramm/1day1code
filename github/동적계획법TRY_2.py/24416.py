#알고리즘수업- 피보나치1
n=int(input())
sum1=1
sum2=0
def fib(n):
    if (n==1 or n==2):
        return 1
    else:
        global sum1
        sum1=sum1+1
        return fib(n-1)+fib(n-2)


d = [0] * 40
def fibo(x):
    if x == 1 or x == 2:
        return 1
    if d[x] != 0:
        return d[x]
    
    d[x] = fibo(x-1) + fibo(x-2)
    return d[x]
fib(n)
print(sum1,n-2)