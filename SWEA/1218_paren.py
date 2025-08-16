import sys; sys.stdin = open('1218_paren.txt')

T = 10
for t in range(1, T+1):
    N = int(input())
    inputs = input()
    param = {')':'(', ']':'[', '}':'{', '>':'<'}

    stack = []
    result = 0
    for ch in inputs:
        if ch in param.values():
            stack.append(ch)
        else:
            if param[ch] == stack[-1]:
                stack.pop()
            else:
                # if len(stack) != 0:
                result = 0
                break

    if len(stack) == 0:
        result = 1
        
    print(f'#{t} {result}')
