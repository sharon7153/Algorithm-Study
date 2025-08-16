import sys
sys.stdin = open('4866_checkParen.txt')

T = int(input())
for t in range(1, T+1):
    string = input()

    stack = []
    paren = {'}':'{', ')':'('}

    valid = 1
    for ch in string:
        if ch in paren.values():
            stack.append(ch)
        elif ch in paren.keys():
            if len(stack) > 0 and stack[-1] == paren[ch]:
                    stack.pop()
            else:
                valid = 0
                break

    if valid == 1 and len(stack) == 0:
        result = 1
    else:
        result = 0

    print(f'#{t} {result}')