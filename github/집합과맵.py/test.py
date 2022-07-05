from collections import deque

a=deque([1,2,3])
a.append(2)
print(a.popleft())
print(a)