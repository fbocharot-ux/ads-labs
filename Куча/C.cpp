#include <iostream>
#include <vector>
#include <string>

using namespace std;

class MinHeap {
private:
    vector<long long> heap;

    void shiftUp(int i) {
        while (i / 2 > 0 && heap[i] < heap[i / 2]) {
            swap(heap[i], heap[i / 2]);
            i = i / 2;
        }
    }

    int indMinChild(int i) {
        int left = 2 * i;
        int right = 2 * i + 1;
        int size = (int)heap.size() - 1;

        if (right > size) {
            return left;
        }
   
        if (heap[left] < heap[right]) {
            return left;
        }
        return right;
    }

    void shiftDown(int i) {
        int size = (int)heap.size() - 1;
        while (2 * i <= size) {
            int j = indMinChild(i);
            if (heap[i] > heap[j]) {
                swap(heap[i], heap[j]);
                i = j;
            }
            else {
                break; 
            }
        }
    }

public:
    MinHeap() {
        heap.push_back(0);
    }

    void clear() {
        heap.clear();
        heap.push_back(0);
    }

    void add(long long x) {
        heap.push_back(x);
        shiftUp((int)heap.size() - 1);
    }

    void extract() {
        int size = (int)heap.size() - 1;
        if (size == 0) {
            cout << "CANNOT\n";
            return;
        }

        long long removed = heap[1];
        heap[1] = heap[size];
        heap.pop_back();

        if ((int)heap.size() - 1 > 0) {
            shiftDown(1);
        }

        cout << removed << "\n";
    }
};

int main() {
    MinHeap minHeap;
    string command;

    while (cin >> command) {
        if (command == "CLEAR") {
            minHeap.clear();
        }
        else if (command == "ADD") {
            long long n;
            cin >> n;
            minHeap.add(n);
        }
        else if (command == "EXTRACT") {
            minHeap.extract();
        }
    }

    return 0;
}
