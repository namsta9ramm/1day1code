def draw(list_use):
    ans1_num=0
    ans2_num=0
    m_list=[]
    n_list=[]
    j_list=[]    
    white_board=['WBWBWBWB'
,'BWBWBWBW','WBWBWBWB','BWBWBWBW','WBWBWBWB','BWBWBWBW','WBWBWBWB','BWBWBWBW']
    black_board=['BWBWBWBW','WBWBWBWB','BWBWBWBW','WBWBWBWB','BWBWBWBW','WBWBWBWB','BWBWBWBW','WBWBWBWB']
    for i in  list_use:
        for p in i:
            m_list.append(p)
    for v in white_board:
        for u in v:
            n_list.append(u)
    for q in black_board:
        for g in q:
            j_list.append(g)
    for ans in range(64):
        if m_list[ans]!=n_list[ans]:
            ans1_num=ans1_num+1
        elif  m_list[ans]!=j_list[ans]:
            ans2_num=ans2_num+1
    return min(ans1_num,ans2_num)

a,b=map(int,input().split())
list_ans=[]
for i in range(a):
    j=input()
    list_ans.append(j)
final_list=[]
for k in range(a-7):
   
    for m in range(b-7):
        new_list=[]
        for j in range(8): 
            
            new_list.append(list_ans[j+k][m:m+8])
        final_list.append(draw(new_list))
print(min(final_list)) 


            
            
        
        
        
