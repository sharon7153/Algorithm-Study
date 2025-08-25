import sys; sys.stdin = open('1231_inorder.txt')

def inorder(node,result):
    # global result
    if node <= N:
        inorder(node*2,result)
        result.append(ch[node])
        # result += ch[node]
        inorder(node*2 + 1,result)
        
T = 10

for t in range(1, T+1):
    N = int(input())

    node = [0]*(N+1)
    ch = ['']*(N+1)
    left = [0]*(N+1)
    right = [0]*(N+1)

    for i in range(1,N+1):
        data = input().split()
        node = int(data[0])
        ch[node] = data[1]
        if len(data) >= 3:
            left[node] = int(data[2])
            if len(data) >= 4:
                right[node] = int(data[3])
    result = []
    # result = ''
    inorder(1,result)
    # inorder(1)
    result_str = ''.join(result)
    print(f'#{t} {result_str}')
    # print(f'#{t} {result}')