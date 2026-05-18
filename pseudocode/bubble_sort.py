from typing import List

def bubble_sort(arr: List[int]) -> List[int]:
    """
    Bubble Sort: Repeatedly swap adjacent elements if in wrong order
    Time: Best O(n), Average O(n²), Worst O(n²)
    Space: O(1)
    Stable: Yes, In-place: Yes
    """
    # Create a copy of the array to avoid modifying the original
    arr = arr.copy()
    n = len(arr)
    
    # Traverse through all array elements
    for i in range(n):
        swapped = False
        # Last i elements are already in place, so we don't need to check them
        for j in range(0, n - i - 1):
            # Traverse the array from 0 to n-i-1
            # Swap if the element found is greater than the next element
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        # If no two elements were swapped by inner loop, the array is sorted
        if not swapped:
            break
    return arr