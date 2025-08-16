import sys
sys.stdin = open('4873_repearWord.txt')

T = int(input())
for t in range(1, T+1):
    string = input()

    stack = []

    for ch in string:
        if len(stack) == 0:
            stack.append(ch)
        else:
            if stack[-1] == ch:
                stack.pop()
            else:
                stack.append(ch)
        # print(stack)
    result = 0
    if stack:
        result = len(stack)

    print(f'#{t} {result}')

