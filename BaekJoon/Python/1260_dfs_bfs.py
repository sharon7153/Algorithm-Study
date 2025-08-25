from collections import deque

def dfs(node):
    global result_1
    if visited_1[node] == 1:
        return
    
    visited_1[node] = 1
    result_1.append(node)  
      
    for next_node in node_arr[node]:
        if visited_1[next_node] == 0:
            dfs(next_node)
    
def bfs(node):
    global result_2
    visited_2[node] = 1
    q = deque()
    q.append(node)
    
    while q:
        if len(q) == 0:
            break
        temp = q.popleft()
        result_2.append(temp)
        
        for ele in node_arr[temp]:
            if visited_2[ele] == 0:
                q.append(ele)
                visited_2[ele] = 1
    

N, M, V = map(int,input().split())

node_arr = [[] for _ in range(N+1)]

for i in range(M):
    s_node, e_node = map(int,input().split())
    node_arr[s_node].append(e_node)
    node_arr[e_node].append(s_node)

# print(node_arr)
for i in range(len(node_arr)):
    if node_arr[i]:
        node_arr[i].sort()
# print(node_arr)
visited_1 = [0]*(N+1)
result_1 = []
dfs(V)
print(*result_1)

visited_2 = [0]*(N+1)
result_2 = []
bfs(V)
print(*result_2)