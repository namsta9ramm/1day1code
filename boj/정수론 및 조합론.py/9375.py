#패션왕 신해빈
test_case=int(input())
f_list=[]
for _ in range(test_case):
    list1=[]
    j=int(input())
    for _ in range(j):
        a,b=input().split()
        list1.append(b)
    s_list=set(list1)  #s_list={h,e}
    ans_list=[]
    
    ans=0
    for i in list(s_list): # for i in [h,e]
                              # list1=[h,e,h]
        ans_list.append(list1.count(i))
    
    r_ans=1
    for k in ans_list:
        r_ans=r_ans*(k+1)
    
    rrans=r_ans-1    
    f_list.append(rrans)

for m in f_list:
    print(m)

