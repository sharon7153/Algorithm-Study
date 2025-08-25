import sys; sys.stdin = open('5102_nodeDistance.txt')

from collections import deque

def bfs(s_node, e_node):
    answer = 0
    q = deque()
    q.append(s_node)
    visitied[s_node] = 1
    
    while q:
        temp = q.popleft()
        if temp == e_node:
            answer = visitied[temp] - 1
            break
        for next_node in node_arr[temp]:
            if visitied[next_node] == 0:
                q.append(next_node)
                visitied[next_node] = visitied[temp] + 1
    return answer

def dfs(s_node, e_node, dist):
    global min_dist
    if s_node == e_node:
        min_dist = min(min_dist, dist)
        return 
    visitied[s_node] = 1
    
    for next_node in node_arr[s_node]:
        if visitied[next_node] == 0:
            dfs(next_node,e_node,dist + 1)
    
    visitied[s_node] = 0



T = int(input())

for t in range(1, T+1):

    V, E = map(int,input().split())

    node_arr = [[] for _ in range(V+1)]
    for _ in range(E):
        node1, node2 = map(int,input().split())
        node_arr[node1].append(node2)
        node_arr[node2].append(node1)

    S, G = map(int,input().split())
    visitied = [0]*(V+1)
    min_dist = float('inf')
    
    result = bfs(S,G)
    print(f'#{t} {result}')
    
    # dfs(S,G,0)
    # print(f'#{t} {min_dist}')