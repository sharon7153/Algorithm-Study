import sys; sys.stdin = open('1234_pwd.txt')

T = 10
for t in range(1, T+1):

    N_str, string = map(str, input().split())

    stack = []
    for ch in string:
        if len(stack) == 0:
            stack.append(ch)
        else:
            if ch == stack[-1]:
                stack.pop()
            else:
                stack.append(ch)

    stack_str = ''.join(stack)
    print(f'#{t} {stack_str}')