#include <iostream>
#include <vector>
#include <cmath>
#include <cstdlib>
#include <ctime>

using namespace std;

// ---------------- MERGE FUNCTION ----------------
vector<int> mergeArrays(const vector<int>& left, const vector<int>& right) {
    vector<int> result;
    int i = 0, j = 0;

    while (i < left.size() && j < right.size()) {
        if (left[i] < right[j]) {
            result.push_back(left[i++]);
        } else {
            result.push_back(right[j++]);
        }
    }

    while (i < left.size())
        result.push_back(left[i++]);

    while (j < right.size())
        result.push_back(right[j++]);

    return result;
}

// ---------------- MERGE SORT ----------------
vector<int> mergeSort(const vector<int>& arr) {
    if (arr.size() <= 1)
        return arr;

    int mid = arr.size() / 2;
    vector<int> left(arr.begin(), arr.begin() + mid);
    vector<int> right(arr.begin() + mid, arr.end());

    left = mergeSort(left);
    right = mergeSort(right);

    return mergeArrays(left, right);
}

// ---------------- BINARY SEARCH ----------------
int binarySearch(const vector<int>& arr, int key, int low, int high) {
    while (low <= high) {
        int mid = low + (high - low) / 2;

        if (arr[mid] == key)
            return mid;
        else if (arr[mid] < key)
            low = mid + 1;
        else
            high = mid - 1;
    }
    return -1;
}

// ---------------- JUMP + BINARY SEARCH ----------------
int jumpBinarySearch(const vector<int>& arr, int key) {
    int n = arr.size();
    int step = sqrt(n);
    int prev = 0;

    while (prev < n && arr[min(step, n) - 1] < key) {
        prev = step;
        step += sqrt(n);
        if (prev >= n)
            return -1;
    }

    return binarySearch(arr, key, prev, min(step, n) - 1);
}

// ---------------- ADAPTIVE SEARCH ----------------
int adaptiveSearch(const vector<int>& arr, int key, int threshold) {
    int n = arr.size();

    if (n > threshold) {
        cout << "Dataset > 1000 → Using MOST OPTIMAL: Binary Search\n";
        return binarySearch(arr, key, 0, n - 1);
    } else {
        cout << "Dataset ≤ 1000 → Using Hybrid: Jump + Binary Search\n";
        return jumpBinarySearch(arr, key);
    }
}

// ---------------- MAIN PROGRAM ----------------
int main() {
    srand(time(0));

    int SIZE;
    const int THRESHOLD = 1000;

    cout << "Enter number of elements to generate: ";
    cin >> SIZE;

    vector<int> arr(SIZE);
    for (int i = 0; i < SIZE; i++) {
        arr[i] = rand() % 10000 + 1;
    }

    cout << "\nRandomly Generated Array:\n";
    for (int x : arr)
        cout << x << " ";
    cout << endl;

    vector<int> sortedArr = mergeSort(arr);

    cout << "\nArray After Merge Sort:\n";
    for (int x : sortedArr)
        cout << x << " ";
    cout << endl;

    int key;
    cout << "\nEnter the element to search: ";
    cin >> key;

    int index = adaptiveSearch(sortedArr, key, THRESHOLD);

    if (index != -1)
        cout << "Element " << key << " found at index " << index << endl;
    else
        cout << "Element " << key << " not found in the array\n";

    return 0;
}
