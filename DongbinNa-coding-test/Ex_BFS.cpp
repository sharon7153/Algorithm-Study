//
// <문제> 미로 탈출
//

#include <iostream>
#include <vector>
#include <queue>

using namespace std;


int N, M;
vector<vector<int>> map;

int bfs(int j, int i)
{
    int dy[4] = {-1, 1, 0 ,0};
    int dx[4] = {0, 0, -1 ,1};

    queue<pair<int, int>> q;
    q.push({j, i});

    while(!q.empty())
    {
        int y = q.front().first;
        int x = q.front().second;
        q.pop();
        
        for(int i = 0; i < 4; i++)
        {
            int ny = y + dy[i];
            int nx = x + dx[i];
            
            if(nx < 0 || nx >= M || ny < 0 || ny >= N)
                continue;
            
            if(map[ny][nx] == 0) 
            {
                continue;
            }
            
            if(map[ny][nx] == 1)
            {
                map[ny][nx] = map[y][x] + 1;
                q.push({ny, nx});
            }
        }
    }

    return map[N-1][M-1];

}

int main()
{
    
    cin >> N >> M;
    map.resize(N, vector<int>(M));

    for(int j = 0; j < N; j++)
    {
        string str;
        cin >> str;
        for(int i = 0; i < M; i++)
        {
            map[j][i] = str[i] - '0';
        }
    }

    cout << bfs(0,0) << endl;
    return 0;
}