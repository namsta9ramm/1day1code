name=input()
testcase=int(input())
ans=[]
for i in range(testcase):
    a,b,c=input().split()
    b=int(b)
    c=int(c)
    new=name[b:c+1]
    ans.append(new.count(a))
for m in ans:
    print(m)