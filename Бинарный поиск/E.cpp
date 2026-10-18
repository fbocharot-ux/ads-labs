#include <iostream>
#include <vector>
using namespace std;

int n, k;
vector<long long> a;

bool distance(long long d) {
    int count = 1;
    long long last = a[0];
    for (int i = 1; i < n; i++) {
        if (a[i] - last >= d) {
            count++;
            last = a[i];
        }
    }
    return count >= k;
}

int main() {
    cin >> n >> k;
    a.resize(n);
    for (int i = 0; i < n; i++) {
        cin >> a[i];
    }

    long long left = 1, right = a[n - 1] - a[0] + 1;
    while (right - left > 1) {
        long long mid = (left + right) / 2;
        if (distance(mid)) {
            left = mid;
        }
        else {
            right = mid;
        }
    }
    cout << left << endl;

    return 0;
}