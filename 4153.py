import sys
while True:
    a,b,c=map(int,sys.stdin.readline().split())
    if a==0 and b==0 and c==0:
        break    
    else:   
        if a<c and b<c:

        
            if a**2+b**2==c**2:
                print("right")
            else:
               print("wrong")
        elif a<b and c<b:

        
            if a**2+c**2==b**2:
                print("right")
            else:
               print("wrong")
        elif b<a and c<a:

        
            if b**2+c**2==a**2:
                print("right")
            else:
               print("wrong")
        
        else:
            print("wrong")