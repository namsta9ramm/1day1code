#숫자 다이얼 전화기
dic={'ABC':3,'DEF':4,'GHI':5,'JKL':6,'MNO':7,'PQRS':8,'TUV':9,'WXYZ':10}
call=input()
call_list=list(call)
sum=0
#call_list=[ABEC]
for k in call_list:
    for key in dic.keys():

        if k in key:
            sum=sum+dic[key]

print(sum)