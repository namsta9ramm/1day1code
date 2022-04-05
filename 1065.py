def han(n):
    sum=0
    if len(str(n))<=2:
        sum=sum+n
        return sum
    elif len(str(n))==3:
        sum=99
        # 1 0 0 , 1 0 1 , 1 0 2 
        for i in range(100,n+1):
            new_list=[int(a) for a in str(i)]
            if new_list[1]-new_list[0]==new_list[2]-new_list[1]:
                sum=sum+1
        return sum
    elif len(str(n))==4:
        return(han(999))

print(han(int(input())))
            

