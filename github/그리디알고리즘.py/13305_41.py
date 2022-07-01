n = int(input())
distnc = list(map(int , input().split())) # distance
cpl =list(map(int, input().split())) # cost per liter
cost_sum = distnc[0]*cpl[0]
min_cost = cpl[0]

for i in range(1, n-1):
    if min_cost > cpl[i]:
        min_cost = cpl[i]
    cost_sum += min_cost * distnc[i]
print(cost_sum)