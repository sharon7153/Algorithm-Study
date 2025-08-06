#include <iostream>
#include <vector>

using namespace std;

int main()
{



    int N, M;
    cin >> N >> M;

    vector<vector<int>> arr(N, vector<int>(N, 0));
    vector<vector<int>> coord(M, vector<int>(4, 0));

    for(int j = 0; j < N; j++)
    {
        for(int i = 0; i < N; i++)
        {
            cin >> arr[j][i];
        }
    }

    for(int j = 0; j < M; j++)
    {
        for(int i = 0; i < 4; i++)
        {
            cin >> coord[j][i];
        }
    }

    for(int n = 0; n < M; n++)
    {
        int x1_idx = coord[n][0] - 1;
        int y1_idx = coord[n][1] - 1;
        int x2_idx = coord[n][2] - 1;
        int y2_idx = coord[n][3] - 1;
        
        int part_sum = 0;
        for(int j = 0; j < N; j++)
        {
            for(int i = 0; i < N; i++)
            {
                if(j >= y1_idx && j <= y2_idx && i >= x1_idx && i <= x2_idx)
                    part_sum += arr[j][i];
            }
        }
        cout << part_sum << endl;
    }


    return 0;
}