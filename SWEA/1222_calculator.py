import sys; sys.stdin = open('1222_calculator.txt')

T = 10
for t in range(1, T+1):
    N = int(input())
    string = input()

    stack = []

    # 후위 표기식으로 변환
    new_string = ''
    for ch in string:
        if ch != '+':
            new_string += ch
        else:
            if len(stack) == 0:
                stack.append(ch)
            else:
                new_string += stack.pop()
                stack.append(ch)
    new_string += stack.pop()
    # print(new_string)

    # 후위 표기식 계산
    new_stack = []
    for ch in new_string:
        if ch != '+':
            new_stack.append(int(ch))
        else:
            a = new_stack.pop()
            b = new_stack.pop()
            
            new_stack.append(a+b)
    result = new_stack.pop()
    print(f'#{t} {result}')