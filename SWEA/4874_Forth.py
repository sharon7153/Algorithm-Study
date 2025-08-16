import sys; sys.stdin = open('4874_Forth.txt')

T = int(input())

for t in range(1, T+1):
    string = list(map(str, input().split()))
    stack = []

    result = ''

    for ch in string:
        if ch not in '+-*/.':
            stack.append(int(ch))
        else:

            if len(stack) < 2 and ch != '.':
                result = 'error'
                break
            if ch == '.':
                if len(stack) != 1:
                    result = 'error'
                    break
                else:
                    result = str(stack.pop())
                    break
            
            a = stack.pop()
            b = stack.pop()
            if ch == '+':   
                stack.append(b + a)
            elif ch == '-':
                stack.append(b - a)
            elif ch == '*':
                stack.append(b * a)
            elif ch == '/':
                stack.append(b // a)

    print(f'#{t} {result}')