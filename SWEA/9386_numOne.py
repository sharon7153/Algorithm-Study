import sys; sys.stdin = open('9386_numOne.txt')

T = int(input())
for t in range(1, T+1):

    N = int(input())
    arr = input()

    count = 0
    max_count = 0
    for ch in arr:
        if ch == '1':
            count += 1
        else:
            if count > 0:
                if max_count < count:
                    max_count = count
                count = 0
        if max_count < count:
            max_count = count

    print(f'#{t} {max_count}')