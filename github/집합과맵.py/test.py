S=input()
ans=[]

for i in range(len(S)):  #i=0 (0,1/1,2/2,3/3,4/)
    for j in range(i,len(S)):  #(0,5)
        temp=S[i:j+1]
        ans.append(temp)
print(ans)
print(len(ans))