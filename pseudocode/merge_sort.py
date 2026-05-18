from typing import List

def merge_sort(arr: List[int]) -> List[int]:
    """
    Merge Sort: Divide and conquer sorting
    Time: O(n log n) all cases
    Space: O(n)
    Stable: Yes, In-place: No
    """
    # Base case: arrays with 0 or 1 element are already sorted
    if len(arr) <= 1:
        return arr.copy()
    
    # Split the array into two halves
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    
    # Merge the sorted halves
    return merge(left, right)

def merge(left: List[int], right: List[int]) -> List[int]:
    """Helper function to merge two sorted arrays"""
    result = []
    i = j = 0
    
    # Compare elements from both lists and append the smaller one
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
            
    # Append any remaining elements
    result.extend(left[i:])
    result.extend(right[j:])
    return result