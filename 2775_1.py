test_case=int(input())
ans_list=[]
for _ in range(test_case):
    
    k=int(input())
    n=int(input())
    array1=[]
    
    
    for j in range(15):
        line=[]
        for i in range(1,15):
            if j==0:
                line.append(i)
            else:
                line.append(sum(array1[j-1][:i]))
        array1.append(line)
    ans_list.append(array1[k][n-1])    
for j in ans_list:
    print(j)

# 너무 복잡하게 푼것같다. .  ㅜㅜ
