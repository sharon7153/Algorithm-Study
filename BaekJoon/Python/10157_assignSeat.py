C, R = map(int,input().split())
K = int(input())

arr = [[0]*C for _ in range(R)]
visited = [[0]*C for _ in range(R)]
num = 1

# C : 가로 , R : 세로
for j in range(C):
    for i in range(R): 
        if visited[R-1-i][j] == 0:
            arr[R-1-i][j] = num
            num += 1
            visited[R-1-i][j] = 1            
    break

# 오른쪽, 아래, 왼쪽, 위
dj = [0, 1, 0, -1]
di = [1, 0, -1, 0]

start_j_idx = 0
start_i_idx = 0
dir = 0
init = 1
count = 0
while 1:
    if init:
        nj = start_j_idx + dj[dir]
        ni = start_i_idx + di[dir]
        init = 0
    else:
        nj += dj[dir]
        ni += di[dir]
        
    if num > C*R:
        break
    
    while 1:
        if nj < 0 or nj >= R or ni < 0 or ni >= C:
            nj = nj - dj[dir]
            ni = ni - di[dir]
            count += 1
            break
        
        if visited[nj][ni] == 1:
            nj = nj - dj[dir]
            ni = ni - di[dir]
            count += 1
            break
        
        if visited[nj][ni] == 0:
            visited[nj][ni] = 1
            arr[nj][ni] = num
            num += 1
            nj = nj + dj[dir]
            ni = ni + di[dir]
    
    dir = count % 4
    
found = 0
for j in range(R):
    for i in range(C):
        if arr[j][i] == K:
            j_idx = j
            i_idx = i
            found = 1
result = []
if found == 0:
    result.append(0)
else:
    result.append(i_idx+1)
    result.append(R-j_idx)
            
print(*result)