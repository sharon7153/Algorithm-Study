N, M = map(int,input().split())

arr = [list(map(int, input().split())) for _ in range(N)]
coord = [list(map(int, input().split())) for _ in range(M)]



for n in range(M):
    x1_idx = coord[n][0] - 1
    y1_idx = coord[n][1] - 1
    x2_idx = coord[n][2] - 1
    y2_idx = coord[n][3] - 1
    part_sum = 0
    for j in range(N):
        for i in range(N):
            if y1_idx <= j <= y2_idx and x1_idx <= i <= x2_idx:
                part_sum += arr[j][i]
    
    print(part_sum)
                

            
            