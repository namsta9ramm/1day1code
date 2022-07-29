from collections import deque

import sys
a=int(sys.stdin.readline())
ans=deque([])
for i in range(a):
    case=sys.stdin.readline().split()
    if case[0]=='push_back':
        
        ans.append(case[1])
    
    elif case[0]=='push_front':
        ans.appendleft(case[1])
    elif case[0]=='size':
        print(len(ans))
    elif case[0]=='empty':

        if len(ans)==0:
            print(1)
        else:
            print(0)
    elif case[0]=='pop_front':
        if len(ans)==0:
            print(-1)
        else:
            print(ans.popleft())
    elif case[0]=='pop_back':
        if len(ans)==0:
            print(-1)
        else:
            print(ans.pop())
    elif case[0]=='front':
        if len(ans)!=0:
            print(ans[0])

        else:
            print(-1)
    elif case[0]=='back':
        if len(ans)!=0:
            print(ans[-1])
        else:
            print(-1)
