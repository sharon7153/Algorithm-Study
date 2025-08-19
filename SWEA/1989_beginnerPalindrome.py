import sys; sys.stdin = open('1989_beginnerPalindrome.txt')
def check_palindrome(arr):
    result = 1
    n = len(arr)
    for i in range(n//2):
        if arr[i] != arr[n-1-i]:
            result = 0
            break
    return result

T = int(input())

for t in range(1, T+1):
    inputs = list(input())
    result = check_palindrome(inputs)  

    print(f'#{t} {result}')