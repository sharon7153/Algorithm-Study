//
// <문제> 음료수 얼려 먹기
//

#include <iostream>
#include <vector>
#include <string>

using namespace std;

bool dfs(int x, int y, vector<vector<int>> &arr)
{
    if(x < 0 || x >= arr[0].size() || y < 0 || y >= arr.size())
        return false;

    if(arr[y][x] == 0)
    {
        arr[y][x] = 1;

        dfs(x - 1, y, arr);
        dfs(x + 1, y, arr);
        dfs(x, y - 1, arr);
        dfs(x, y + 1, arr);

        return true;
    }
    return false;
}

int main()
{
    int N, M;
    cin >> N >> M;

    vector<vector<int>> arr(N,vector<int>(M));

    for(int j = 0; j < N; j++)
    {
        string str;
        cin >> str;

        for(int i = 0; i < M; i++)
        {
            arr[j][i] = str[i] - '0';
        }
    }

    int count = 0;
    for(int j = 0; j < N; j++)
    {
        for(int i = 0; i < M; i++)
        {
            if(dfs(i, j, arr) == true)
                count += 1;
        }
    }

    cout << count << endl;
    return 0;
}