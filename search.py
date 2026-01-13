# import random
# import math
# import time

# # ---------------- MERGE SORT ----------------
# def merge_sort(arr):
#     if len(arr) <= 1:
#         return arr

#     mid = len(arr) // 2
#     left = merge_sort(arr[:mid])
#     right = merge_sort(arr[mid:])

#     return merge(left, right)

# def merge(left, right):
#     result = []
#     i = j = 0

#     while i < len(left) and j < len(right):
#         if left[i] < right[j]:
#             result.append(left[i])
#             i += 1
#         else:
#             result.append(right[j])
#             j += 1

#     result.extend(left[i:])
#     result.extend(right[j:])
#     return result


# # ---------------- BINARY SEARCH ----------------
# def binary_search(arr, key):
#     low, high = 0, len(arr) - 1

#     while low <= high:
#         mid = (low + high) // 2
#         if arr[mid] == key:
#             return mid
#         elif arr[mid] < key:
#             low = mid + 1
#         else:
#             high = mid - 1
#     return -1


# # ---------------- JUMP + BINARY SEARCH ----------------
# def jump_binary_search(arr, key):
#     n = len(arr)
#     step = int(math.sqrt(n))
#     prev = 0

#     while prev < n and arr[min(step, n) - 1] < key:
#         prev = step
#         step += int(math.sqrt(n))
#         if prev >= n:
#             return -1

#     return binary_search(arr[prev:min(step, n)], key)


# # ---------------- MAIN PROGRAM ----------------
# if __name__ == "__main__":

#     SIZE = int(input("Enter number of elements to generate: "))

#     # Generate random array
#     arr = [random.randint(1, 100000) for _ in range(SIZE)]

#     # Merge sort
#     sorted_arr = merge_sort(arr)

#     print("\nSorted Array:")
#     print(sorted_arr)

#     # Element to search
#     key = int(input("\nEnter the element to search: "))

#     # -------- Binary Search Timing --------
#     start = time.perf_counter()
#     index_bs = binary_search(sorted_arr, key)
#     end = time.perf_counter()
#     time_bs = end - start

#     # -------- Jump + Binary Search Timing --------
#     start = time.perf_counter()
#     index_hybrid = jump_binary_search(sorted_arr, key)
#     end = time.perf_counter()
#     time_hybrid = end - start

#     # -------- Output --------
#     print("\n--- SEARCH RESULTS ---")

#     if index_bs != -1:
#         print(f"Binary Search: FOUND (Index = {index_bs})")
#     else:
#         print("Binary Search: NOT FOUND")

#     print(f"Binary Search Time: {time_bs:.8f} seconds")

#     print()

#     if index_hybrid != -1:
#         print("Jump + Binary Search: FOUND")
#     else:
#         print("Jump + Binary Search: NOT FOUND")

#     print(f"Jump + Binary Search Time: {time_hybrid:.8f} seconds")



# #jump +binary 










import random
import math
import time

# MERGE SORT
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


# LINEAR SEARCH
def linear_search(arr, key):
    for i in range(len(arr)):
        if arr[i] == key:
            return i
    return -1


# JUMP + LINEAR SEARCH
def jump_linear_search(arr, key):
    n = len(arr)
    step = int(math.sqrt(n))
    prev = 0

    # Jumping phase
    while prev < n and arr[min(step, n) - 1] < key:
        prev = step
        step += int(math.sqrt(n))
        if prev >= n:
            return -1

    # Linear search in the block
    for i in range(prev, min(step, n)):
        if arr[i] == key:
            return i

    return -1


# MAIN PROGRAM
if __name__ == "__main__":

    SIZE = int(input("Enter number of elements to generate: "))

    # Generate random array
    arr = [random.randint(1, 100000) for _ in range(SIZE)]

    # Sort array (needed for Jump Search)
    sorted_arr = merge_sort(arr)

    print("\nSorted Array:")
    print(sorted_arr)

    key = int(input("\nEnter the element to search: "))

    # Linear Search Timing
    start = time.perf_counter()
    index_linear = linear_search(sorted_arr, key)
    end = time.perf_counter()
    time_linear = end - start

    # Jump + Linear Search Timing
    start = time.perf_counter()
    index_jump = jump_linear_search(sorted_arr, key)
    end = time.perf_counter()
    time_jump = end - start

    # -------- Output --------
    print("\n--- SEARCH RESULTS ---")

    if index_linear != -1:
        print(f"Linear Search: FOUND (Index = {index_linear})")
    else:
        print("Linear Search: NOT FOUND")

    print(f"Linear Search Time: {time_linear:.8f} seconds\n")

    if index_jump != -1:
        print(f"Jump + Linear Search: FOUND (Index = {index_jump})")
    else:
        print("Jump + Linear Search: NOT FOUND")

    print(f"Jump + Linear Search Time: {time_jump:.8f} seconds")



# jump linear 