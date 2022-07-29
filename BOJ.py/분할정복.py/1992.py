a=int(input())
list1=[]
for i in range(a):
    list1.append(list(input()))

ans_a=''
def solution(x,y,n):
    global ans_a
    color=list1[x][y]
    for i in range(x,x+n):
        for j in range(y,y+n):
            if color!=list1[i][j]:
                ans_a=ans_a+"("
                solution(x,y,n//2)
                solution(x,y+n//2,n//2)
                solution(x+n//2,y,n//2)
                
                solution(x+n//2,y+n//2,n//2)
                ans_a=ans_a+")"
                return 
            
    if color=='0':
        ans_a=ans_a+'0'  
    else:
        ans_a=ans_a+'1'

solution(0,0,a)

print(ans_a)
