import sys

a,b=(map(str,sys.stdin.readline().split()))

a1=int(a[::-1])
a2=int(b[::-1])


if a1>a2:
    print(a1)
else:
    print(a2)