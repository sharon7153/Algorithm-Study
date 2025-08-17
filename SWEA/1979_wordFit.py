import sys; sys.stdin = open('1979_wordFit.txt')

T = int(input())

for t in range(1, T+1):

    N, K = map(int,input().split())
    arr = [list(map(int,input().split())) for _ in range(N)]
    
    row = []
    col = []
    for j in range(N):
        count_row = 0
        count_col = 0
        for i in range(N):
            # 행 기준 연속된 1의 값 저장
            if arr[j][i] == 1:
                count_row += 1
            else:
                if count_row > 0:
                    row.append(count_row)
                    count_row = 0
                    
            # 열 기준 연속된 1의 값 저장
            if arr[i][j] == 1:
                count_col += 1
            else:
                if count_col > 0:
                    row.append(count_col)
                    count_col = 0
                    
        if count_row > 0:
            row.append(count_row)
        if count_col > 0:
            col.append(count_col)

    result = 0
    for ele in row:
        if ele == K:
            result += 1
    for ele in col:
        if ele == K:
            result += 1

    print(f'#{t} {result}')