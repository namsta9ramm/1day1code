#알파벳이 대소문자로 주어진다
#가장 많이 사용된 알파벳이 무엇인지 출력하기
#Missippi
a=input()
b=a.upper()   #MISSIPPI
new_list=list(set(b)) # MISP
ans_list=[]   #[1,3,2,2]
for i in new_list:
    
        ans_list.append(b.count(i))

if ans_list.count(max(ans_list))>1:
    print("?")

else:
    k=ans_list.index(max(ans_list))
    print(new_list[k])
