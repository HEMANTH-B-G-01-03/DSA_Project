# import random
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


# # ---------------- LINEAR SEARCH (SINGLE ALGORITHM) ----------------
# def linear_search(arr, key):
#     for i in range(len(arr)):
#         if arr[i] == key:
#             return i
#     return -1


# # ---------------- INTERPOLATION + LINEAR SEARCH (HYBRID) ----------------
# def interpolation_linear_search(arr, key):
#     low = 0
#     high = len(arr) - 1

#     while low <= high and key >= arr[low] and key <= arr[high]:
#         if arr[low] == arr[high]:
#             break

#         # Interpolation formula
#         pos = low + int(
#             ((high - low) / (arr[high] - arr[low])) * (key - arr[low])
#         )

#         # Small linear window around estimated position
#         window = 5
#         start = max(low, pos - window)
#         end = min(high, pos + window)

#         for i in range(start, end + 1):
#             if arr[i] == key:
#                 return i

#         if key < arr[start]:
#             high = start - 1
#         else:
#             low = end + 1

#     return -1


# # ---------------- MAIN PROGRAM ----------------
# if __name__ == "__main__":

#     SIZE = int(input("Enter number of elements to generate: "))

#     # Generate random array
#     arr = [random.randint(1, 100000) for _ in range(SIZE)]

#     print("\n🔹 Randomly Generated Array:")
#     print(arr)

#     # Sort array
#     sorted_arr = merge_sort(arr)

#     print("\n🔹 After sorting the array using Merge Sort:")
#     print(sorted_arr)

#     # Element to search
#     key = int(input("\nEnter the element to search: "))

#     # -------- Linear Search Timing --------
#     start = time.perf_counter()
#     index_linear = linear_search(sorted_arr, key)
#     end = time.perf_counter()
#     time_linear = end - start

#     # -------- Interpolation + Linear Search Timing --------
#     start = time.perf_counter()
#     index_hybrid = interpolation_linear_search(sorted_arr, key)
#     end = time.perf_counter()
#     time_hybrid = end - start

#     # -------- Output --------
#     print("\n🔹 SEARCH RESULTS")

#     if index_linear != -1:
#         print(f"Linear Search: Element FOUND at index {index_linear}")
#     else:
#         print("Linear Search: Element NOT FOUND")

#     print(f"Linear Search Time Taken: {time_linear:.8f} seconds")

#     print()

#     if index_hybrid != -1:
#         print(f"Interpolation + Linear Search: Element FOUND at index {index_hybrid}")
#     else:
#         print("Interpolation + Linear Search: Element NOT FOUND")

#     print(f"Interpolation + Linear Search Time Taken: {time_hybrid:.8f} seconds")










# # table form is bellow 

# import random
# import time
# import matplotlib.pyplot as plt

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


# # ---------------- LINEAR SEARCH ----------------
# def linear_search(arr, key):
#     for i in range(len(arr)):
#         if arr[i] == key:
#             return i
#     return -1


# # ---------------- INTERPOLATION + LINEAR SEARCH ----------------
# def interpolation_linear_search(arr, key):
#     low, high = 0, len(arr) - 1

#     while low <= high and key >= arr[low] and key <= arr[high]:
#         if arr[low] == arr[high]:
#             break

#         pos = low + int(
#             ((high - low) / (arr[high] - arr[low])) * (key - arr[low])
#         )

#         window = 5
#         start = max(low, pos - window)
#         end = min(high, pos + window)

#         for i in range(start, end + 1):
#             if arr[i] == key:
#                 return i

#         if key < arr[start]:
#             high = start - 1
#         else:
#             low = end + 1

#     return -1


# # ---------------- MAIN PROGRAM ----------------
# if __name__ == "__main__":

#     sizes = [10, 50, 100, 1000, 5000, 10000]
#     results = []

#     for n in sizes:
#         print("\n==============================================")
#         print(f"Number of elements (n) = {n}")

#         # Generate random numbers
#         arr = [random.randint(1, 100000) for _ in range(n)]
#         print(f"\nThe generated random {n} numbers are:")
#         print(arr)

#         # Sort using merge sort
#         sorted_arr = merge_sort(arr)
#         print("\nAfter Merge Sort, the sorted array elements are:")
#         print(sorted_arr)

#         # Ask element to search (FOR EACH n)
#         key = int(input("\nEnter the element to be searched from these numbers: "))

#         # Linear search timing
#         start = time.perf_counter()
#         linear_search(sorted_arr, key)
#         time_linear = time.perf_counter() - start

#         # Hybrid search timing
#         start = time.perf_counter()
#         interpolation_linear_search(sorted_arr, key)
#         time_hybrid = time.perf_counter() - start

#         results.append([n, f"{time_linear:.8f}", f"{time_hybrid:.8f}"])

#     # ---------------- PRINT TABLE IN TERMINAL ----------------
#     print("\n\n============= COMPARISON TABLE =============")
#     print("-" * 75)
#     print(f"{'Total Elements':<20}{'Linear Search (s)':<25}{'Interpolation + Linear (s)'}")
#     print("-" * 75)

#     for row in results:
#         print(f"{row[0]:<20}{row[1]:<25}{row[2]}")

#     print("-" * 75)

#     # ---------------- SAVE TABLE AS JPG ----------------
#     fig, ax = plt.subplots()
#     ax.axis('off')

#     table = ax.table(
#         cellText=results,
#         colLabels=["Total Elements", "Linear Search (s)", "Interpolation + Linear (s)"],
#         loc='center'
#     )

#     table.scale(1, 1.5)
#     plt.title("Comparison of Linear Search vs Interpolation + Linear Search")

#     plt.savefig("search_comparison_table.jpg", dpi=300, bbox_inches='tight')
#     plt.show()

#     print("\n✅ JPG file created: search_comparison_table.jpg")






import random
import time
import matplotlib.pyplot as plt

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


# ---------------- INTERPOLATION + LINEAR SEARCH ----------------
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

    sizes = [10, 50, 100, 1000, 5000, 10000]
    results = []

    for n in sizes:
        print("\n==============================================")
        print(f"Number of elements (n) = {n}")

        # Generate random numbers
        arr = [random.randint(1, 100000) for _ in range(n)]
        print(f"\nThe generated random {n} numbers are:")
        print(arr)

        # Sort using merge sort
        sorted_arr = merge_sort(arr)
        print("\nAfter Merge Sort, the sorted array elements are:")
        print(sorted_arr)

        # Ask element to search
        key = int(input("\nEnter the element to be searched from these numbers: "))

        # Linear search timing
        start = time.perf_counter()
        linear_search(sorted_arr, key)
        time_linear = time.perf_counter() - start

        # Hybrid search timing
        start = time.perf_counter()
        interpolation_linear_search(sorted_arr, key)
        time_hybrid = time.perf_counter() - start

        # Time difference
        time_difference = time_linear - time_hybrid

        # Print enhancement message
        if time_difference > 0:
            print(f"⏱️ Time has been enhanced by {time_difference:.8f} seconds using Interpolation + Linear Search")
        else:
            print(f"⚠️ Hybrid search took {-time_difference:.8f} seconds more than Linear Search")

        results.append([
            n,
            f"{time_linear:.8f}",
            f"{time_hybrid:.8f}",
            f"{time_difference:.8f}"
        ])

    # ---------------- PRINT TABLE IN TERMINAL ----------------
    print("\n\n============= COMPARISON TABLE =============")
    print("-" * 95)
    print(f"{'Total Elements':<20}{'Linear Search (s)':<25}"
          f"{'Interpolation + Linear (s)':<30}{'Time Enhanced (s)'}")
    print("-" * 95)

    for row in results:
        print(f"{row[0]:<20}{row[1]:<25}{row[2]:<30}{row[3]}")

    print("-" * 95)

    # ---------------- SAVE TABLE AS JPG ----------------
    fig, ax = plt.subplots()
    ax.axis('off')

    table = ax.table(
        cellText=results,
        colLabels=[
            "Total Elements",
            "Linear Search (s)",
            "Interpolation + Linear (s)",
            "Time Enhanced (s)"
        ],
        loc='center'
    )

    table.scale(1, 1.5)
    plt.title("Comparison of Linear Search vs Interpolation + Linear Search")

    plt.savefig("search_comparison_table.jpg", dpi=300, bbox_inches='tight')
    plt.show()

    print("\n✅ JPG file created: search_comparison_table.jpg")
