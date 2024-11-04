import random
import time

# Bubble Sort with Early Exit
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:  # Stop if no elements were swapped
            break
    return arr

# In-place Quick Sort
def quick_sort(arr, low=0, high=None):
    if high is None:
        high = len(arr) - 1
    if low < high:
        pivot_index = partition(arr, low, high)
        quick_sort(arr, low, pivot_index - 1)
        quick_sort(arr, pivot_index + 1, high)
    return arr

def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

# Hybrid Merge Sort with Insertion Sort for small subarrays
def hybrid_merge_sort(arr, threshold=10):
    if len(arr) <= threshold:
        return insertion_sort(arr)
    
    mid = len(arr) // 2
    left = hybrid_merge_sort(arr[:mid], threshold)
    right = hybrid_merge_sort(arr[mid:], threshold)
    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

# Function to compare sorting algorithms' performance
def compare_sorting_algorithms(arr):
    algorithms = [
        ("Bubble Sort", bubble_sort),
        ("Quick Sort", lambda x: quick_sort(x, 0, len(x) - 1)),
        ("Hybrid Merge Sort", hybrid_merge_sort)
    ]
    
    for name, func in algorithms:
        arr_copy = arr.copy()
        start_time = time.time()
        func(arr_copy)
        end_time = time.time()
        print(f"{name} took {end_time - start_time:.6f} seconds")

# Generate a test array and test each sorting function
test_arr = [64, 34, 25, 12, 22, 11, 90]

# Test each sorting algorithm individually
sorted_arr_bubble = bubble_sort(test_arr.copy())
print("Bubble Sort Result:", sorted_arr_bubble)

sorted_arr_quick = quick_sort(test_arr.copy())
print("Quick Sort Result:", sorted_arr_quick)

sorted_arr_hybrid_merge = hybrid_merge_sort(test_arr.copy())
print("Hybrid Merge Sort Result:", sorted_arr_hybrid_merge)

# Generate a large random array for performance comparison
large_arr = [random.randint(1, 1000) for _ in range(1000)]

# Compare the algorithms' performance
compare_sorting_algorithms(large_arr)
