import sys

a,b=map(int,sys.stdin.readline().split())
c,d=map(int,sys.stdin.readline().split())
e,f=map(int,sys.stdin.readline().split())

if a==c and b==d:
    print(e,f)

elif a==c and b==f:
    print(e,d)
elif a==e and b==d:
    print(c,f)
elif a==e and b==f:
    print(c,d)
elif c==e and b==d:
    print(a,f)
elif c==e and b==f:
    print(a,d)
elif a==c and d==f:
    print(e,b)
elif a==e and d==f:
    print(c,b)
elif c==e and d==f:
    print(a,b)

