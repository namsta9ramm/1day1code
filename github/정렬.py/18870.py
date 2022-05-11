import sys
#인덱스로 값을 찾으면 시간복잡도가 올라간다.
input = sys.stdin.readline

n = int(input())
list_1 = list(map(int, input().split()))

list_2= sorted(list(set(list_1)))
dic = {list_2[i] : i for i in range(len(list_2))}

for i in list_1:
    print(dic[i], end = ' ')


    
