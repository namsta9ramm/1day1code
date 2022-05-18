a,b=map(int,input().split())

def gcd(a,b):
    while b:
        a,b=b,a%b
    return a

print(gcd(a,b))

def lcm(a,b):
    result= (a*b)//gcd(a,b)
    return result

print(lcm(a,b))