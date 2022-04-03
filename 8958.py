n=int(input())
for _ in range(n):
    new_list=list(input())

    score=0
    sum_score=0
    for i in new_list:
        if i=='O':
            score=score+1
            sum_score=sum_score+score
        else:
            score=0
    print(sum_score)