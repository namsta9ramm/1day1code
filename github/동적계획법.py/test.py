num = int(input())
group_word = 0
error = 0
# num= 5
# word= aa , ab , ba , bb , abc
for i in range(num):
    word = input() #bb
    for i in range(len(word)-1): #1
        
        if word[i] != word[i+1]:
            if word[i+1:].count(word[i])>0:
                error += 1
    
    
    if error == 0:
        group_word += 1

    print(group_word)
print(group_word)