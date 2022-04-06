#크로아티아 알파벳 
#여러가지 방면으로 생각해봐야 하는문제
a=['c=','c-','dz=','d-','lj','nj','s=','z=']
word=input()
for i in a:
    if i in word:
        word=word.replace(i,"*")

print(len(word)) 
