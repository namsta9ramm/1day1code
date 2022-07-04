n,m = map(int,input().split())
card = list(map(int, input().split()))
card_diff = max(card) # 3
ans = 0
for i in range(n): # range(5)
    for j in range(i+1,n): # n=5 i= 0 range(1,5)
        for k in range(j+1, n):
            if 0 <= m - (card[i] + card[j] + card[k]) <= card_diff: 
                ans = card[i] + card[j] + card[k]
                print(i,j,k)
                card_diff = m - (card[i] + card[j] + card[k])

print(ans)
#5 21
#5 6 7 8 9  o<=21-18<=9 ans=18 