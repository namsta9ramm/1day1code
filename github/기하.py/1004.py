#어린왕자
test_case=int(input())

ans_list=[]
for _ in range(test_case):
    ans1_num=0
    
    x1,y1,x2,y2=map(int,input().split())
    num1=int(input())
    for _ in range(num1):
        c1,c2,r=map(int,input().split())
        if ((x1-c1)**2+(y1-c2)**2)**0.5<r and ((x2-c1)**2+(y2-c2)**2)**0.5>r:

            ans1_num=ans1_num+1
        elif ((x1-c1)**2+(y1-c2)**2)**0.5>r and ((x2-c1)**2+(y2-c2)**2)**0.5<r:
            ans1_num=ans1_num+1
    
    ans_list.append(ans1_num)

for i in ans_list:
    print(i)