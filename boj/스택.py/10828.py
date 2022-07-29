import sys
a=int(sys.stdin.readline())
ans=[]
for i in range(a):
    case=sys.stdin.readline().split()
    if case[0]=='push':
        
        ans.append(case[1])
    elif case[0]=='top':
        if len(ans)==0:
            print(-1)
        else:
            print(ans[-1])
    elif case[0]=='size':
        print(len(ans))
    elif case[0]=='empty':

        if len(ans)==0:
            print(1)
        else:
            print(0)
    elif case[0]=='pop':
        if len(ans)==0:
            print(-1)
        else:
            print(ans.pop())

