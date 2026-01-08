import random
import math

# ---------------- MERGE SORT ----------------
def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])
    return result


# ---------------- BINARY SEARCH ----------------
def binary_search(arr, key, low, high):
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == key:
            return mid
        elif arr[mid] < key:
            low = mid + 1
        else:
            high = mid - 1
    return -1


# ---------------- JUMP + BINARY SEARCH ----------------
def jump_binary_search(arr, key):
    n = len(arr)
    step = int(math.sqrt(n))
    prev = 0

    while prev < n and arr[min(step, n) - 1] < key:
        prev = step
        step += int(math.sqrt(n))
        if prev >= n:
            return -1

    return binary_search(arr, key, prev, min(step, n) - 1)


# ---------------- ADAPTIVE SEARCH ----------------
def adaptive_search(arr, key, threshold):
    n = len(arr)

    if n > threshold:
        print("Dataset > 1000 → Using MOST OPTIMAL: Binary Search")
        return binary_search(arr, key, 0, n - 1)
    else:
        print("Dataset ≤ 1000 → Using Hybrid: Jump + Binary Search")
        return jump_binary_search(arr, key)


# ---------------- MAIN PROGRAM ----------------
if __name__ == "__main__":

    # Dynamic size input
    SIZE = int(input("Enter number of elements to generate: "))
    THRESHOLD = 1000

    # Generate random array
    arr = [random.randint(1, 10000) for _ in range(SIZE)]

    print("\n Randomly Generated Array:")
    print(arr)

    # Merge sort
    sorted_arr = merge_sort(arr)

    print("\n Array After Merge Sort:")
    print(sorted_arr)

    # User input for element to search
    key = int(input("\n Enter the element to search: "))

    # Adaptive search
    index = adaptive_search(sorted_arr, key, THRESHOLD)

    if index != -1:
        print(f" Element {key} found at index {index}")
    else:
        print(f" Element {key} not found in the array")
 