#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main()
{
    int N;
    cin >> N;

    vector<int> arr(N);

    for(int i = 0; i < N; i++)
    {
        cin >> arr[i];
    }

    sort(arr.begin(), arr.end());

    int group  = 0;
    int count = 0;
    for(int i = 0; i < N; i++)
    {
        count += 1;
        if(count >= arr[i])
        {
            group++;
            count = 0;
        }
        
    }



    // sort(arr.rbegin(), arr.rend());

    // int i = 0;
    // int max_n = arr[i];
    // int group = 0;

    // while(1)
    // {
    //     if(arr.empty())
    //         break;
        
        
    //     arr.erase(arr.begin());
    //     for(int i = 0; i < max_n - 1; i++)
    //     {
    //         arr.pop_back();
    //     }

    //     max_n = arr[0];
    //     group++;
    // }

    cout << group << endl;

    return 0;

}