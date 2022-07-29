#50+60-70+90-100
a1=input().split('-') #[50+60, 70+90 ,100]
new_array=[]  #[55,50+40]
for i in a1:
    if '+' in i:
        a=i.split('+')
        sum=0
        for j in a:
            sum=sum+int(j)
        new_array.append(sum)
    else:
        new_array.append(int(i))
    
a1=new_array[0]

for j in range(1,len(new_array)):
    a1=a1-new_array[j] 
print(a1)   
