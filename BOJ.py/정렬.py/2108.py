#통계학 산술평균, 중앙값, 최빈값 , 범위
import sys
from collections import Counter
n=int(input())
list_num=[]
for _ in range(n):
    list_num.append(int(sys.stdin.readline()))
#산술평균
print(round(sum(list_num)/n))

#중앙값
list_num.sort()
if len(list_num)%2==0:
    print(list_num[(len(list_num)//2)-1])

else:
    print(list_num[len(list_num)//2])

#최빈값
cnt=Counter(list_num).most_common()
if len(cnt)>1 and cnt[0][1]==cnt[1][1]:
  print(cnt[1][0])
else :
  print(cnt[0][0])


print(list_num[-1]-list_num[0])