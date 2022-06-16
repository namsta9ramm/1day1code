#N-Queen
def adjacent(x): 
    for i in range(x): 
        if row[x] == row[i] or abs(row[x] - row[i]) == x - i: # 열이 같거나(row[x] == row[i]) 대각선이 같은경우  false
            return False 
    return True
 
#한줄씩 재귀하며 dfs 실행
 
def dfs(x):
    global result
 
    if x == N:
        result += 1
    else:
        # 각 행에 퀸 놓기
        for i in range(N): # i 는 열번호 0부터 N 전까지 옮겨가면서 유망한곳 찾기
            row[x] = i
            if adjacent(x): # 행,열,대각선 체크함수 true이면 계속진행
                dfs(x + 1)
 

N = int(input())
row = [0] * N
result = 0
dfs(0)
print(result)
