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


# ---------------- LINEAR SEARCH (SINGLE ALGORITHM) ----------------
def linear_search(arr, key):
    for i in range(len(arr)):
        if arr[i] == key:
            return i
    return -1


# ---------------- INTERPOLATION + LINEAR SEARCH (HYBRID) ----------------
def interpolation_linear_search(arr, key):
    low = 0
    high = len(arr) - 1

    while low <= high and key >= arr[low] and key <= arr[high]:
        if arr[low] == arr[high]:
            break

        # Interpolation formula
        pos = low + int(
            ((high - low) / (arr[high] - arr[low])) * (key - arr[low])
        )

        # Small linear window around estimated position
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

    SIZE = int(input("Enter number of elements to generate: "))

    # Generate random array
    arr = [random.randint(1, 100000) for _ in range(SIZE)]

    print("\n🔹 Randomly Generated Array:")
    print(arr)

    # Sort array
    sorted_arr = merge_sort(arr)

    print("\n🔹 After sorting the array using Merge Sort:")
    print(sorted_arr)

    # Element to search
    key = int(input("\nEnter the element to search: "))

    # -------- Linear Search Timing --------
    start = time.perf_counter()
    index_linear = linear_search(sorted_arr, key)
    end = time.perf_counter()
    time_linear = end - start

    # -------- Interpolation + Linear Search Timing --------
    start = time.perf_counter()
    index_hybrid = interpolation_linear_search(sorted_arr, key)
    end = time.perf_counter()
    time_hybrid = end - start

    # -------- Output --------
    print("\n🔹 SEARCH RESULTS")

    if index_linear != -1:
        print(f"Linear Search: Element FOUND at index {index_linear}")
    else:
        print("Linear Search: Element NOT FOUND")

    print(f"Linear Search Time Taken: {time_linear:.8f} seconds")

    print()

    if index_hybrid != -1:
        print(f"Interpolation + Linear Search: Element FOUND at index {index_hybrid}")
    else:
        print("Interpolation + Linear Search: Element NOT FOUND")

    print(f"Interpolation + Linear Search Time Taken: {time_hybrid:.8f} seconds")
