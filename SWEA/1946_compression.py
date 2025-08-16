import sys; sys.stdin = open('1946_compression.txt')

T = int(input())
for t in range(1, T+1):

    N = int(input())
    C = [0]*N
    K = [0]*N

    total_len = 0
    total_string = ''

    for i in range(N):
        C[i], K[i] = map(str,input().split())
        

    for i in range(N): 
        n = int(K[i])
        for j in range(n):
            total_string += C[i]
        total_len += n
    
    print(f'#{t}')
    count = 0
    for i in range(total_len):
        count += 1
        if count % 10 == 0:
            print(total_string[i])
        else:
            print(total_string[i], end='')
    if count % 10 != 0:
        print()
        