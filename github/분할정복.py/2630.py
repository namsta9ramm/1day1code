a=int(input())
list1=[]
for i in range(a):
    list1.append(list(map(int,input().split())))

blue=0
white=0

def solution(x,y,n):
    global blue,white
    color=list1[x][y]
    for i in range(x,x+n):
        for j in range(y,y+n):
            if color!=list1[i][j]:
                solution(x,y,n//2)
                solution(x+n//2,y,n//2)
                solution(x,y+n//2,n//2)
                solution(x+n//2,y+n//2,n//2)
                return
    if color==0:
        white=white+1
    else:
        blue=blue+1

solution(0,0,a)
print(white)
print(blue)
