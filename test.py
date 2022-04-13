def print_star(a):
    ans_list=[]

    for i in range(a):
    
        for j in range(a):
            
            ans_list.append('*')
            
            if a//3<=i<a//3+a//3 and a//3<=j<a//3+a//3:

        print()
    return print_star(a//3)

k=int(input())
print(print_star(k))