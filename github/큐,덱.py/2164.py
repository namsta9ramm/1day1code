#N장의 카드
from collections import deque
a=int(input())
ans=deque([])
for i in range(1,a+1):
    ans.append(i)

while len(ans)!=1:
    ans.popleft()
    b=ans[0]
    ans.append(b)
    ans.popleft()
print(*ans)

