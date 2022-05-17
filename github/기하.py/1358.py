#아이스링크장 h 는 짝수 
w,h,x,y,p=map(int,input().split())
c=0
for _ in range(p):
    
    a,b=map(int,input().split())
    if x<=a<=x+w and y<=b<=y+h:
        c=c+1
    elif a<x:
        if ((x-a)**2+(y+0.5*h-b)**2)**0.5<=0.5*h:
            c=c+1
    elif x+w<a:
        if ((x+w-a)**2+(y+0.5*h-b)**2)**0.5<=0.5*h:
            c=c+1
print(c)