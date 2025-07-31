#include <iostream>
#include <string>
#include <algorithm>
#include <cctype>
#include <vector>

using namespace std;

int main()
{
    string input;
    cin >> input;

    int sum = 0;

    sort(input.begin(), input.end());

    string arr;
    for(int i = 0; i < input.size(); i++)
    {
        if(isdigit(input[i]))
            sum += (input[i] - '0'); 
        else
            arr.push_back(input[i]);
    }
    
    if(sum != 0)
        arr += to_string(sum);

    for(int i = 0; i < arr.size(); i++)
    {
        cout << arr[i];
    }
    
    

    return 0;
}