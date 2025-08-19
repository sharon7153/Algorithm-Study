import sys; sys.stdin = open('1215_palindrome1.txt')

def check_palindrome(arr):
    result = 1
    n = len(arr)
    for i in range(n//2):
        if arr[i] != arr[n-1-i]:
            result = 0
            break
    return result

T = 10

for t in range(1, T+1):

    N = int(input())
    arr = [input() for _ in range(8)]

    count = 0
    for j in range(8):
        for i in range(8-N+1):
            temp_row = ''
            for n in range(i, i+N):
                temp_row += arr[j][n]
            if check_palindrome(temp_row):
                count += 1
            
            temp_col = ''
            for n in range(i, i+N):
                temp_col += arr[n][j]
            if check_palindrome(temp_col):
                count += 1
            
    print(f'#{t} {count}')