#include <iostream>
#include <vector>

using namespace std;



int main()
{
    int N, K;
    cin >> N >> K;
    
    vector<int> A(N);
    vector<int> B(N);

    for(int i = 0; i < N; i ++)
    {
        cin >> A[i] >> B[i];
    }

    int left = 0;
    int right = 1e9;
    int answer = -1;

    
    while(left <= right)
    {
        int mid = (left + right) / 2;
        int count = 0;

        for(int i = 0, j = 0; i < A.size() && j < B.size(); i++, j++)
        {
            if(A[i] + mid >= B[i])
            {
                count++;
            }
        }

        if(count >= K)
        {
            answer = mid;
            right = mid - 1;
        }
        else
        {
            left = mid + 1;
        }
         
    }

    cout << answer << endl;


    return 0;
}