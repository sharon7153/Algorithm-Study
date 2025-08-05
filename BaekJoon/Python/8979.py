N,K = map(int, input().split())

arr = [[0]*4 for _ in range(N)]

for i in range(N):
    arr[i][0], arr[i][1], arr[i][2], arr[i][3] = map(int,input().split())

target = []

for i in range(N):
    if arr[i][0] == K:
        target = arr[i]

rank = 1

for i in range(N):
    if arr[i][0] == target[0]:
        continue
    
    if arr[i][1] > target[1]:
        rank += 1
    elif arr[i][1] == target[1] and arr[i][2] > target[2]:
        rank += 1
    elif arr[i][1] == target[1] and arr[i][2] == target[2] and arr[i][3] > target[3]:
        rank += 1

print(rank)