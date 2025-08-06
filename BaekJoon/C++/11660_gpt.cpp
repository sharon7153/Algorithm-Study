#include <iostream>
#include <vector>

using namespace std;

int main() {
    ios::sync_with_stdio(false);  // 속도 최적화
    cin.tie(NULL);

    int N, M;
    cin >> N >> M;

    vector<vector<int>> arr(N + 1, vector<int>(N + 1, 0));
    vector<vector<int>> sum(N + 1, vector<int>(N + 1, 0));

    // 입력 받기
    for (int i = 1; i <= N; i++) {
        for (int j = 1; j <= N; j++) {
            cin >> arr[i][j];
        }
    }

    // 누적합 계산
    for (int i = 1; i <= N; i++) {
        for (int j = 1; j <= N; j++) {
            sum[i][j] = arr[i][j] + sum[i-1][j] + sum[i][j-1] - sum[i-1][j-1];
        }
    }

    // 쿼리 처리
    for (int q = 0; q < M; q++) {
        int x1, y1, x2, y2;
        cin >> x1 >> y1 >> x2 >> y2;

        int result = sum[x2][y2] 
                   - sum[x1-1][y2] 
                   - sum[x2][y1-1] 
                   + sum[x1-1][y1-1];

        cout << result << "\n";
    }

    return 0;
}
