#include <iostream>
#include <vector>
#include <sstream>
#include <string>
using namespace std;

vector<int> counting_sort(vector<int>& arr) {
    int min_val = arr[0];
    int max_val = arr[0];
    for (int i = 1; i < (int)arr.size(); i++) {
        if (arr[i] < min_val) min_val = arr[i];
        if (arr[i] > max_val) max_val = arr[i];
    }
    vector<int> count(max_val - min_val + 1, 0);

    for (int i = 0; i < (int)arr.size(); i++) {
        count[arr[i] - min_val]++;
    }

    int index = 0;
    for (int i = 0; i < (int)count.size(); i++) {
        for (int k = 0; k < count[i]; k++) {
            arr[index] = min_val + i;
            index++;
        }
    }

    return arr;
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

    vector<int> result = counting_sort(arr);
    for (int i = 0; i < (int)result.size(); i++) {
        cout << result[i] << " ";
    }
    cout << endl;
    return 0;
}
