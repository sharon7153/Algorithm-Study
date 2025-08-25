import sys; sys.stdin = open('1223_calculator2.txt')

T = 10

for t in range(1, T+1):

    N = int(input())
    inputs = input()

    # 후위 표기식 변환
    op = {'+':1, '*':2}
    stack = []
    post_inputs = ''
    for token in inputs:
        if token not in '*+':
            post_inputs += token
        else:
            if len(stack) == 0:
                stack.append(token)
            else:
                while 1:
                    if len(stack) == 0 or op[stack[-1]] < op[token]:
                        break
                    if op[stack[-1]] >= op[token]:
                        post_inputs += stack.pop()
                stack.append(token)
    while stack:
        temp = stack.pop()
        # print(temp)
        post_inputs += temp
    # print(post_inputs)

    # 후위 표기식 계산
    num = []
    for token in post_inputs:
        if token not in '*+':
            num.append(int(token))
        else:
            a = num.pop()
            b = num.pop()
            
            if token == '*':
                num.append(a*b)
            else:
                num.append(a+b)

    print(f'#{t} {num.pop()}')

