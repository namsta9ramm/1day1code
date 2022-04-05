# 생각정리 만약 입력한 WHAT 안에 
what='abcdefghijklmnopqrstuvwxyz'
S=input()
new_list=[str(i) for i in what]
S_list=[str(k) for k in S]
#new_list=[a,b,c,d,,,,z]
#S=beakjoon
ans_list=[]
for k in new_list:
    if k in S:
        ans_list.append(S_list.index(k))
    else:
        ans_list.append(-1)
for i in ans_list:
    print(i, end=" ")
