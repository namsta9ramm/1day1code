import sys
a=int(input())
score=list[a]

score=list(map(int,sys.stdin.readline().split()))

result_score=[]
for i in score:
    result_score.append((i/max(score))*100)

sum=0
for i in result_score:
    sum=sum+i

print(sum/len(result_score))
