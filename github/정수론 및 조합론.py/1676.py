import math

a=int(input())

new_str=str(math.factorial(a))
new_f_str=new_str.rstrip('0')
print(len(new_str)-len(new_f_str))