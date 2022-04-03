import sys
a=int(input())

for _ in range(a):
    score=list(map(int,sys.stdin.readline().split()))
    sum=0
    aver=0
    for k in range(1,len(score)):
        sum=sum+score[k]
    aver=sum/(len(score)-1)
    count=0
    for j in range(1,len(score)):
        if score[j]>aver:
            count=count+1
    
    print("{:.3f}%".format(100*(count/(len(score)-1))))

