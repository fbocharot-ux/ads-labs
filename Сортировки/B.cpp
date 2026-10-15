#include <iostream>
#include <vector>
#include <sstream>
#include <string>
using namespace std;

void InsertionSort(vector<int>& arr) {
    for (int i = 1; i < (int)arr.size(); i++) {
        int elem = arr[i];
        int index = i - 1;
        while (index >= 0 && arr[index] > elem) {
            arr[index + 1] = arr[index];
            index = index - 1;
        }
        arr[index + 1] = elem;
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

    InsertionSort(arr);
    for (int i = 0; i < (int)arr.size(); i++) {
        cout << arr[i] << " ";
    }
    cout << endl;
    return 0;
}