a=int(input())
list1=[]
for i in range(a):
    list1.append(list(map(int,input().split())))
num_1=0
num_2=0
num_rev1=0
def solution(x,y,n):
    global num_1,num_2,num_rev1
    color=list1[x][y]
    for i in range(x,x+n):
        for j in range(y,y+n):
            if color!=list1[i][j]:
                solution(x,y,n//3)
                solution(x+n//3,y,n//3)
                solution(x+2*n//3,y,n//3)
                solution(x,y+n//3,n//3)
                solution(x+n//3,y+n//3,n//3)
                solution(x+2*n//3,y+n//3,n//3)
                solution(x,y+2*n//3,n//3)
                solution(x+n//3,y+2*n//3,n//3)
                solution(x+2*n//3,y+2*n//3,n//3)
                return 
    if color==1:
        num_1=num_1+1
    elif color==0:
        num_2=num_2+1
    else:
        num_rev1=num_rev1+1

solution(0,0,a)
print(num_rev1)
print(num_2)
print(num_1)
