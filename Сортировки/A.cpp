#include <iostream>
#include <vector>
#include <sstream>
#include <string>
using namespace std;

void SelectionSort(vector<int>& a) {
    for (int i = 0; i < (int)a.size() - 1; i++) {
        int max_index = i;
        for (int j = i + 1; j < (int)a.size(); j++) {
            if (a[j] > a[max_index]) {
                max_index = j;
            }
        }
        swap(a[i], a[max_index]);
    }
}

int main() {
    string line;
    getline(cin, line);
    stringstream ss(line);
    vector<int> a;
    int x;
    while (ss >> x) {
        a.push_back(x);
    }

    SelectionSort(a);
    for (int i = 0; i < (int)a.size(); i++) {
        cout << a[i] << " ";
    }
    cout << endl;
    return 0;
}