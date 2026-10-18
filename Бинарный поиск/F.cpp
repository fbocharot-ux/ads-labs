#include <iostream>
using namespace std;

long long n, x, y;
long long quick, slow;

bool min_time(long long T) {
    return T / quick + T / slow >= n - 1;
}

int main() {
    cin >> n >> x >> y;

    quick = min(x, y);
    slow = max(x, y);

    long long left = 0, right = (n - 1) * slow;
    while (right - left > 1) {
        long long mid = (left + right) / 2;
        if (min_time(mid)) {
            right = mid;
        }
        else {
            left = mid;
        }
    }

    cout << quick + right << endl;

    return 0;
}