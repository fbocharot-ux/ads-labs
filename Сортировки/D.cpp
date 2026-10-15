#include <iostream>
#include <vector>
using namespace std;

int bubble_sort(vector<int>& arr) {
    int count_change = 0;
    for (int i = 0; i < (int)arr.size() - 1; i++) {
        bool swapped = false;
        for (int j = 0; j < (int)arr.size() - i - 1; j++) {
            if (arr[j] > arr[j + 1]) {
                swap(arr[j], arr[j + 1]);
                swapped = true;
                count_change++;
            }
        }
        if (!swapped) {
            break;
        }
    }
    return count_change;
}

int main() {
    int n;
    cin >> n;
    vector<int> arr(n);
    for (int i = 0; i < n; i++) {
        cin >> arr[i];
    }
    cout << bubble_sort(arr) << endl;
    return 0;
}