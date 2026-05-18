from typing import List

def insertion_sort(arr: List[int]) -> List[int]:
    """
    Insertion Sort: Build sorted array one element at a time
    Time: Best O(n), Average O(n²), Worst O(n²)
    Space: O(1)
    Stable: Yes, In-place: Yes
    """
    # Create a copy of the array to avoid modifying the original
    arr = arr.copy()
    
    # Traverse through 1 to len(arr)
    for i in range(1, len(arr)):
        key = arr[i]
        # Move elements of arr[0..i-1], that are greater than key,
        # to one position ahead of their current position
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr