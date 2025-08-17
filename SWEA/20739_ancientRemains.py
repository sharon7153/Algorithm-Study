import sys; sys.stdin = open('20739_ancientRemains.txt')

T = int(input())

for t in range(1, T+1):

    N, M = map(int,input().split())

    arr = [list(map(int,input().split())) for _ in range(N)]

    max_count = 0
    for j in range(N):
        count_row = 0
        for i in range(M):
            if arr[j][i] == 1:
                count_row += 1
            else:
                if count_row > 0:
                    if max_count < count_row:
                        max_count = count_row
                    count_row = 0
        if max_count < count_row:
            max_count = count_row
            
    for j in range(M):
        count_col = 0
        for i in range(N):
            if arr[i][j] == 1:
                count_col += 1
            else:
                if count_col > 0:
                    if max_count < count_col:
                        max_count = count_col
                    count_col = 0
        if max_count < count_col:
            max_count = count_col

    if max_count == 1:
        max_count = 0
        
    print(f'#{t} {max_count}')