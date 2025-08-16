import sys
sys.stdin = open('4869_paper.txt')

T = int(input())
for t in range(1, T+1):
    N = int(input())

    def dp(n):
        if n == 0 or n == 1:
            return 1
        else:
            return dp(n-1) + 2*dp(n-2)
        

    n = N // 10
    result = dp(n)

    print(f'#{t} {result}')