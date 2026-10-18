#include <iostream>
#include <vector>
using namespace std;

int n, k;
vector<long long> a;

bool line(long long L) {
    long long cnt = 0;
    for (long long x : a) {
        cnt += x / L;
    }
    return cnt >= k;
}

int main() {
    cin >> n >> k;
    for (int i = 0; i < n; i++) {
        long long x;
        cin >> x;
        a.push_back(x);
    }

    long long left = 0, right = 10000001;
    while (right - left > 1) {
        long long mid = (left + right) / 2;
        if (line(mid)) {
            left = mid;
        }
        else {
            right = mid;
        }
    }
    cout << left << endl;

    return 0;
}