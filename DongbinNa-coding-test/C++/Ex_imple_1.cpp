#include <iostream>
#include <vector>
#include <string>

using namespace std;

int main()
{

    // 북, 남, 동, 서
    int dx[4] = {-1, 1, 0, 0};
    int dy[4] = {0, 0, -1, 1};
    char pos[4] = {'L', 'R', 'U', 'D'};

    int N;
    cin >> N;
    cin.ignore();

    string line;
    getline(cin, line);
    
    int x = 1;
    int y = 1;
    // for(int i = 0; i < line.size(); i++)
    // {
    //     if(y == 0)  y = 1;
    //     if(y == N+1) y = N;
    //     if(x == 0)  x = 1;
    //     if(x == N+1) x = N;
        
    //     if(x >= 1 && y >=1){
    //         if(line[i] == pos[0]){
    //             x += dx[0];
    //             y += dy[0];
    //             // cout << "L" << " ";
    //         }else if(line[i] == pos[1]){
    //             x += dx[1];
    //             y += dy[1];
    //             // cout << "R" << " ";
    //         }else if(line[i] == pos[2]){
    //             x += dx[2];
    //             y += dy[2];
    //             // cout << "U" << " ";
    //         }else if(line[i] == pos[3]){
    //             x += dx[3];
    //             y += dy[3];
    //             // cout << "D" << " ";
    //         }
    //     }
    //     // cout << y <<" " << x << endl;
    // }


    for(int i = 0; i < line.size(); i++)
    {
        int nx = -1, ny = -1;
        for(int j = 0; j < 4; j++)
        {
            if(line[i] == pos[j])
            {   
                nx = x + dx[j];
                ny = y + dy[j];
            }
        }
        if(nx < 1 || ny < 1 || nx > N || ny > N)
            continue;
        x = nx;
        y = ny;
    }

    cout << y <<" " << x << endl;

    return 0;
}