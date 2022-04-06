#크로아티아 알파벳 
a=['c=','c-','dz=','d-','lj','nj','s=','z=']
word=input()
for i in a:
    if i in word:
        word=word.replace(i,"*")

print(len(word))
