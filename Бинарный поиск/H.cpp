#include <iostream>
using namespace std;

long long w, h, n;

bool diplom_rast(long long X) {
    return (X / w) * (X / h) >= n;
}

int main() {
    cin >> w >> h >> n;

    long long left = 0, right = max(w, h) * n;
    while (right - left > 1) {
        long long mid = (left + right) / 2;
        if (diplom_rast(mid)) {
            right = mid;
        }
        else {
            left = mid;
        }
    }
    cout << right << endl;

    return 0;
}