num=int(input())
stair=[0]*301
score=[0]*301
for k in range(num):
    stair[k]=int(input())
score[0]=stair[0]
score[1]=stair[0]+stair[1]
score[2]=stair[2]+max(stair[0],stair[1])


for i in range(3,num+1):
    score[i]=stair[i]+max(stair[i-1]+score[i-3],score[i-2])

print(score[num-1])