from typing import List

def selection_sort(arr: List[int]) -> List[int]:
    """
    Selection Sort: Find minimum and place at beginning
    Time: O(n²) all cases
    Space: O(1)
    Stable: No, In-place: Yes
    """
    # Create a copy of the array to avoid modifying the original
    arr = arr.copy()
    n = len(arr)
    
    # Traverse through all array elements
    for i in range(n):
        # Find the minimum element in the remaining unsorted array
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
                
        # Swap the found minimum element with the first element of the unsorted part
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr