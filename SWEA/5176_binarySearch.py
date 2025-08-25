import sys; sys.stdin = open('5176_binarySearch.txt')

def inorder(node):
    global count
    
    if node <= N:
        inorder(node*2)
        tree[node] = count
        count += 1
        inorder(node*2+1)
    

T = int(input())

for t in range(1,T+1):
    N = int(input())

    tree = [0]*(N+1)
    count = 1
    inorder(1)
    print(f'#{t} {tree[1]} {tree[N//2]}')