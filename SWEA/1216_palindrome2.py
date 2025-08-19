import sys; sys.stdin = open('1216_palindrome2.txt')

def check_palindrome(arr):
    result = 1
    n = len(arr)
    for i in range(n//2):
        if arr[i] != arr[n-1-i]:
            result = 0
            break
    return result

T = 10

for _ in range(1, T+1):
    t = int(input())
    N = 100
    arr = [input() for _ in range(N)]

    max_length_row = 0
    found_row = 0
    for m in range(N, 0, -1):
        for j in range(N):
            for i in range(N-m+1):
                temp_row = ''
                for n in range(i, i+m):
                    temp_row += arr[j][n]
                if check_palindrome(temp_row):
                    # print(temp_row)
                    # print(j,i)
                    max_length_row = m 
                    found_row = 1
                    break  
            if found_row == 1:
                break
        if found_row == 1:
                break
                
    max_length_col = 0 
    found_col = 0     
    for m in range(N, 0, -1):
        for j in range(N):
            for i in range(N-m+1):          
                temp_col = ''
                for n in range(i, i+m):
                    temp_col += arr[n][j]
                if check_palindrome(temp_col):
                    # print(temp_col) 
                    # print(j,i)
                    max_length_col = m
                    found_col = 1
                    break  
            if found_col == 1:
                break
        if found_col == 1:
                break

    result = max(max_length_row, max_length_col)
    print(f'#{t} {result}')