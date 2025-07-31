#include <iostream>
#include <string>

using namespace std;

int main()
{
    int N;
    cin >> N;

    int count = 0;
    for(int h = 0; h <= N; h++)
    {
        // string h_str = to_string(h);
        // if(h_str.find('3') != string::npos)
        //     count++;

        for(int m = 0; m < 60; m++)
        {
            // string m_str = to_string(m);
            // if(m_str.find('3') != string::npos)
            //     count++;

            for(int s = 0; s < 60; s++)
            {
                // string s_str = to_string(s);
                // if(s_str.find('3') != string::npos)
                //     count++;
                string time = to_string(h) + to_string(m) + to_string(s);
                if(time.find('3') != string::npos)
                    count++;
            }

        }
    }

    cout << count << endl;


    return 0;
}