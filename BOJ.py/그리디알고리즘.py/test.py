n = int(input())
room = []

for i in range(n):
    a, b = map(int, input().split())
    room.append([a, b])


room.sort(key = lambda x: x[1])

for j in room:
    print(j)