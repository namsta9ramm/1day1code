#균형잡힌세상
ans_list=[]
while True:
    a=input()
    list_o=[0]*100
    
    if a==".":
        break
    for j in a:
        if j=="(":
            list_o.append('1')
        elif j=="[":
            list_o.append('2')
        elif j==")":

            if list_o[-1]=='1':
                list_o.pop()
            else:
                list_o.append(")")
        elif j=="]":
            if list_o[-1]=='2':
                list_o.pop()
            else:
                list_o.append(")")
              
    if '1' not in list_o and '2' not in list_o and len(list_o)==100:
        ans_list.append("yes")
    else:
        ans_list.append("no")
for m in ans_list:
    print(m)