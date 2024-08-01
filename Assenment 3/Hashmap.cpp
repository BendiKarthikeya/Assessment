#include <iostream>
#include <vector>
#include <utility>

using namespace std;

class LinearProbingHashMap {
private:
    vector<pair<int, int>> table;
    vector<bool> isOccupied;
    int capacity;
    int size;

    int hash(int key) {
        return key % capacity;
    }

    int probe(int key, int i) {
        return (hash(key) + i) % capacity;
    }

public:
    LinearProbingHashMap(int cap) : capacity(cap), size(0) {
        table.resize(capacity, {-1, -1});
        isOccupied.resize(capacity, false);
    }

    void insert(int key, int value) {
        if (size >= capacity) {
            cout << "HashMap is full" << endl;
            return;
        }
        int i = 0;
        int idx;
        while (true) {
            idx = probe(key, i);
            if (!isOccupied[idx] || table[idx].first == key) break;
            i++;
        }
        if (!isOccupied[idx]) size++;
        table[idx] = {key, value};
        isOccupied[idx] = true;
    }

    bool find(int key) {
        int i = 0;
        int idx;
        while (true) {
            idx = probe(key, i);
            if (!isOccupied[idx]) return false;
            if (table[idx].first == key) return true;
            i++;
        }
    }

    void remove(int key) {
        int i = 0;
        int idx;
        while (true) {
            idx = probe(key, i);
            if (!isOccupied[idx]) return;
            if (table[idx].first == key) {
                isOccupied[idx] = false;
                size--;
                return;
            }
            i++;
        }
    }
};
