import sys
from collections import Counter
n=int(input())
list_num=[]
for _ in range(n):
    list_num.append(int(sys.stdin.readline()))

#최빈값

cnt=Counter(list_num).most_common()
print(cnt)
if len(cnt)>1 and cnt[0][1]==cnt[1][1]:
  print(cnt[1][0])
else :
  print(cnt[0][0])
