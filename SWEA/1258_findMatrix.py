import sys; sys.stdin = open('1258_findMatrix.txt')

T = int(input())

for t in range(1, T+1):
    N = int(input())
    arr = [list(map(int,input().split())) for _ in range(N)]
    result_list = []
    
    for j in range(N):
        for i in range(N):
            if arr[j][i] != 0:
                # 열 
                col = i
                while 1:
                    if arr[j][col] == 0 and col < N:
                        break
                    col += 1
                col_length = col - i
        
                # 행
                row = j
                while 1:
                    if arr[row][i] == 0 and row < N:
                        break
                    row += 1
                row_length = row - j
                
                result_list.append((row_length, col_length))
                # print(result_list)
                for r in range(j, j + row_length):
                    for c in range(i, i + col_length):
                        arr[r][c] = 0
        


    # for i in range(N):  
    #     print(arr[i])
    # print(result_list)

    result_list.sort(key=lambda x: (x[0]*x[1],x[0]))
    print(f'#{t} {len(result_list)}', end=" ")
    for ele in result_list:
        print(ele[0], ele[1], end=" ")
    print()

