import math

# Modified Linear Search Function: Returns all indices where target appears
def linear_search(arr, target):
    indices = []
    comparisons = 0
    for i in range(len(arr)):
        comparisons += 1
        if arr[i] == target:
            indices.append(i)
    return indices, comparisons

# Binary Search for Insertion Point
def binary_search_insertion_point(arr, target):
    left, right = 0, len(arr) - 1
    comparisons = 0
    while left <= right:
        mid = (left + right) // 2
        comparisons += 1
        if arr[mid] == target:
            return mid, comparisons
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return left, comparisons  # Left is the insertion point if target not found

# Jump Search Implementation
def jump_search(arr, target):
    n = len(arr)
    step = int(math.sqrt(n))  # Optimal jump size is √n
    prev, comparisons = 0, 0
    
    # Jump in blocks until target is likely within range
    while arr[min(step, n) - 1] < target:
        comparisons += 1
        prev = step
        step += int(math.sqrt(n))
        if prev >= n:
            return -1, comparisons  # Target not found
    
    # Linear search within block
    for i in range(prev, min(step, n)):
        comparisons += 1
        if arr[i] == target:
            return i, comparisons
    return -1, comparisons

# Comparison of Search Algorithms
def search_comparison(arr, target):
    linear_result, linear_comparisons = linear_search(arr, target)
    insertion_point, binary_comparisons = binary_search_insertion_point(arr, target)
    jump_result, jump_comparisons = jump_search(arr, target)
    
    print("Linear Search Results:", linear_result, "Comparisons:", linear_comparisons)
    print("Binary Search Insertion Point:", insertion_point, "Comparisons:", binary_comparisons)
    print("Jump Search Result:", jump_result, "Comparisons:", jump_comparisons)

# Example Usage
arr = [1, 3, 5, 7, 7, 7, 9, 11]
target = 7
search_comparison(arr, target)
