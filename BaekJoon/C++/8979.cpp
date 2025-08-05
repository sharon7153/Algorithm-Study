#include <iostream>
#include <vector>

using namespace std;

int main()
{
    int N, K;
    cin >> N >> K;

    vector<vector<int>> arr(N, vector<int>(4,0));

    for(int i = 0; i < N; i++)
    {
        cin >> arr[i][0] >> arr[i][1] >> arr[i][2] >> arr[i][3];
    }

    vector<int> target;
    for(int i = 0; i < N; i++)
    {
        if(arr[i][0] == K)
        {
            target = arr[i];
            break;
        }
    }

    int rank = 1;
    for(int i = 0; i < N; i++)
    {
        if(arr[i][0] == target[0]) 
            continue;
        
        if(arr[i][1] > target[1])
            rank++;
        else if(arr[i][1] == target[1] && arr[i][2] > target[2])
            rank++;
        else if(arr[i][1] == target[1] && arr[i][2] == target[2] && arr[i][3] > target[3])
            rank++;
    }

    cout << rank << endl;

    return 0;
}