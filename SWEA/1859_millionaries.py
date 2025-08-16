import sys; sys.stdin = open('1859_millionaries.txt')

T = int(input())
for t in range(1, T+1):

    N = int(input())
    arr = list(map(int, input().split()))

    max_value = arr[N-1]       
    profit = 0
    for i in range(N-2, -1, -1):
        if max_value > arr[i]:
            profit += (max_value - arr[i])
        else:
            max_value = arr[i]

    print(f'#{t} {profit}')