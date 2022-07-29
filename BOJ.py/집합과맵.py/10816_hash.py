#숫자카드2
#숫자카드는 정수 하나씩 적혀있는 카드이다..
#상근이는 숫자 카드 n개를 가지고 있다. 정수 m 개가 주어졌을때.
#상근이가 몇개 가지고 있나
from sys import stdin
_ = stdin.readline()
N = map(int,stdin.readline().split())
_ = stdin.readline()
M = map(int,stdin.readline().split())
hashmap = {}
for n in N:
    if n in hashmap:
        hashmap[n] += 1
    else:
        hashmap[n] = 1

print(' '.join(str(hashmap[m]) if m in hashmap else '0' for m in M))