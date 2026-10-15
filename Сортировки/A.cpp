#include <iostream>
#include <vector>
#include <sstream>
#include <string>
using namespace std;

void SelectionSort(vector<int>& arr) {
    for (int i = 0; i < (int)arr.size() - 1; i++) {
        int max_index = i;
        for (int j = i + 1; j < (int)a.size(); j++) {
            if (arr[j] > arr[max_index]) {
                max_index = j;
            }
        }
        swap(arr[i], arr[max_index]);
    }
}

int main() {
    string line;
    getline(cin, line);
    stringstream ss(line);
    vector<int> arr;
    int x;
    while (ss >> x) {
        arr.push_back(x);
    }

    SelectionSort(arr);
    for (int i = 0; i < (int)arr.size(); i++) {
        cout << arr[i] << " ";
    }
    cout << endl;
    return 0;
}
