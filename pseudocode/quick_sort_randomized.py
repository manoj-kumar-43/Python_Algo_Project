from typing import List

def quick_sort_randomized(arr: List[int]) -> List[int]:
    """
    Quick Sort (Randomized): Random element as pivot
    Time: Best O(n log n), Average O(n log n), Worst O(n²) rare
    Space: O(log n)
    Stable: No, In-place: Yes
    """
    # Create a copy to sort in-place without modifying the original
    arr = arr.copy()
    _quick_sort_helper(arr, 0, len(arr) - 1, randomized=True)
    return arr

def _quick_sort_helper(arr, low, high, randomized):
    """Recursive helper function for Quick Sort"""
    if low < high:
        # pi is partitioning index, arr[pi] is now at right place
        pi = _partition(arr, low, high, randomized)
        
        # Separately sort elements before and after partition
        _quick_sort_helper(arr, low, pi - 1, randomized)
        _quick_sort_helper(arr, pi + 1, high, randomized)

def _partition(arr, low, high, randomized):
    """
    This function takes the last element as pivot (after potentially swapping it
    with a random element), places the pivot element at its correct position in
    sorted array, and places all smaller elements to left of pivot and all
    greater elements to right of pivot.
    """
    if randomized:
        import random
        # Select a random pivot and swap it with the last element
        random_idx = random.randint(low, high)
        arr[random_idx], arr[high] = arr[high], arr[random_idx]
    
    pivot = arr[high]
    i = low - 1  # Index of smaller element
    
    for j in range(low, high):
        # If current element is smaller than or equal to pivot
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
            
    # Place the pivot element at its correct position
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1