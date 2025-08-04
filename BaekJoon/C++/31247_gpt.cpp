#include <iostream>
#include <vector>

using namespace std;

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int T;
    cin >> T;

    vector<long long> result;
    
    for(int i = 0; i < T; i++)
    {
        long long N, K;
        cin >> N >> K;

        if(K >= 64)
        {
            result.push_back(0);
        }
        else
        {
            long long denom = 1LL << K;
            if(denom > N)
            {
                result.push_back(0);
            }
            else
            {
                long long m = N / denom;
                long long count = (m + 1) / 2;
                result.push_back(count);
            }
        }
    }

    for(int i = 0; i < result.size(); i++)
        cout << result[i] << '\n';

    return 0;
}
