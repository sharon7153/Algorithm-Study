import sys; sys.stdin = open('9489_ancientRuin.txt')

T = int(input())

for t in range(1, T+1):

    N, M = map(int,input().split())
    arr = [list(map(int,input().split())) for _ in range(N)]

    row_count = 0
    for i in range(N):
        count = 0
        for j in range(M):
            if arr[i][j] == 1:
                count += 1
            else:
                if count > 0:
                    if row_count < count:
                        row_count = count
                    count = 0
        if row_count < count:
            row_count = count
    # print(row_count)

    col_count = 0
    for i in range(M):
        count = 0
        for j in range(N):
            if arr[j][i] == 1:
                count += 1
            else:
                if count > 0:
                    if col_count < count:
                        col_count = count
                    count = 0
        if col_count < count:
            col_count = count
    # print(col_count)

    max_count = max(row_count, col_count)

    if max_count == 1:
        max_count = 0

    print(f'#{t} {max_count}')