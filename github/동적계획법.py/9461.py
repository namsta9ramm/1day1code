#파도반수열
testcase=int(input())
#1<=n<=100
ans_list=[]
list_n=[0]*101
list_n[1]=1
list_n[2]=1
list_n[3]=1
list_n[4]=2
for _ in range(testcase):
    a=int(input())
    for i in range(5,a+1):
        list_n[i]=list_n[i-3]+list_n[i-2]
    
    print(list_n[a])