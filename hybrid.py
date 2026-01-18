import random
import time

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


# ---------------- LINEAR SEARCH ----------------
def linear_search(arr, key):
    for i in range(len(arr)):
        if arr[i] == key:
            return i
    return -1


# ---------------- INTERPOLATION SEARCH ----------------
def interpolation_search(arr, key):
    low, high = 0, len(arr) - 1

    while low <= high and key >= arr[low] and key <= arr[high]:
        if arr[low] == arr[high]:
            break

        pos = low + int(
            ((high - low) / (arr[high] - arr[low])) * (key - arr[low])
        )

        if arr[pos] == key:
            return pos
        elif arr[pos] < key:
            low = pos + 1
        else:
            high = pos - 1

    return -1


# ---------------- INTERPOLATION + LINEAR SEARCH (HYBRID) ----------------
def interpolation_linear_search(arr, key):
    low, high = 0, len(arr) - 1

    while low <= high and key >= arr[low] and key <= arr[high]:
        if arr[low] == arr[high]:
            break

        pos = low + int(
            ((high - low) / (arr[high] - arr[low])) * (key - arr[low])
        )

        window = 5
        start = max(low, pos - window)
        end = min(high, pos + window)

        for i in range(start, end + 1):
            if arr[i] == key:
                return i

        if key < arr[start]:
            high = start - 1
        else:
            low = end + 1

    return -1


# ---------------- MAIN PROGRAM ----------------
if __name__ == "__main__":

    n = int(input("Enter number of elements to generate: "))

    arr = [random.randint(1, 10000) for _ in range(n)]

    print("\nGenerated Random Numbers:")
    print(arr)

    sorted_arr = merge_sort(arr)

    print("\nAfter Merge Sort:")
    print(sorted_arr)

    key = int(input("\nEnter the element to be searched: "))

    # -------- LINEAR SEARCH --------
    idx_linear = linear_search(sorted_arr, key)
    print("\nLinear Search:")
    if idx_linear != -1:
        print(f"Element FOUND at index {idx_linear}")
    else:
        print("Element NOT FOUND")

    # -------- INTERPOLATION SEARCH --------
    idx_interp = interpolation_search(sorted_arr, key)
    print("\nInterpolation Search:")
    if idx_interp != -1:
        print(f"Element FOUND at index {idx_interp}")
    else:
        print("Element NOT FOUND")

    # -------- HYBRID SEARCH (WITH TIME) --------
    start_time = time.perf_counter()
    idx_hybrid = interpolation_linear_search(sorted_arr, key)
    end_time = time.perf_counter()

    hybrid_time = (end_time - start_time) * 1_000_000  

    print("\nInterpolation + Linear (Hybrid) Search:")
    if idx_hybrid != -1:
        print(f"Element FOUND at index {idx_hybrid}")
    else:
        print("Element NOT FOUND")

    print(f"Time taken by the developed Hybrid Search is: {hybrid_time:.3f} microseconds")
