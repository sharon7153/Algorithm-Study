#include <iostream>
#include <vector>

using namespace std;

vector<int> cal_division(int n)
{
    vector<int> result;
    for(int i = 1; i < n+1; i++)
    {
        if(n % i == 0)
        {
            result.push_back(i);
        }
    }

    return result;

}

int main()
{
    int T;
    cin >> T;

    vector<int> N(T);
    vector<int> K(T);

    for(int i = 0; i < T; i++)
    {
        cin >> N[i] >> K[i];
    }

    for(int i = 0; i < T; i++)
    {
        int n = N[i];
        int k = K[i];

        int count_k = 0;
        while(n > 0)
        {
            int count_even = 0;
            int count_odd = 0;
            vector<int> arr = cal_division(n);
            for(int j = 0; j < arr.size(); j++)
            {
                if(arr[j] % 2 == 0)
                    count_even++;
                else
                    count_odd++;
            }

            if(count_even == k*count_odd)
                count_k++;
            n--;
        }
        cout << count_k << endl;
    }

    return 0;
}