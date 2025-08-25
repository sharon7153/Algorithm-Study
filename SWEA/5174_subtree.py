import sys; sys.stdin = open('5174_subtree.txt')

def count_subtree_recur(node):
    global count_r

    count_r += 1
  
    for next_node in adj[node]:
        count_subtree_recur(next_node)

            
def count_subtree(node):
    global count
    visitied = [0]*(E+2)
    visitied[node] = 1

    q = []
    q.append(node)

    while 1:
        temp = q.pop(0)
       
        if len(adj[temp]) == 0:
            break
        for next_node in adj[temp]:
            q.append(next_node)
            count += 1  
        

T = int(input())

for t in range(1, T+1):

    E, N = map(int,input().split())
    arr = list(map(int,input().split()))

    adj = [[] for _ in range(E+2)]

    for i in range(0,E*2,2):
        adj[arr[i]].append(arr[i+1])

    # count = 1
    # count_subtree(N)
    # print(f'#{t} {count}')
    
    count_r = 0
    count_subtree_recur(N)
    print(f'#{t} {count_r}')
