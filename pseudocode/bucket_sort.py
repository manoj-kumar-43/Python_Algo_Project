from typing import List

def bucket_sort(arr: List[int]) -> List[int]:
    """
    Bucket Sort: Distribute into buckets and sort
    Time: Best O(n + k), Average O(n + k), Worst O(n²)
    Space: O(n + k)
    Stable: Yes, In-place: No
    """
    if not arr:
        return arr.copy()
    
    # Determine the range of values and the size of each bucket
    min_val, max_val = min(arr), max(arr)
    # Add 1 to bucket_range to handle the case where max_val is in the last bucket
    bucket_range = (max_val - min_val) / len(arr) + 1
    
    # Create empty buckets
    buckets = [[] for _ in range(len(arr))]
    
    # Distribute input array values into buckets
    for num in arr:
        # Calculate the index of the bucket for the current number
        index = int((num - min_val) / bucket_range)
        # Ensure the index is within the valid range
        if index >= len(arr):
            index = len(arr) - 1
        buckets[index].append(num)
    
    # Sort individual buckets and concatenate the results
    result = []
    for bucket in buckets:
        # Use a simple sorting algorithm like insertion sort for small buckets
        result.extend(insertion_sort(bucket))
    
    return result


def insertion_sort(arr: List[int]) -> List[int]:
    """
    Insertion Sort: Build sorted array one element at a time
    Time: Best O(n), Average O(n²), Worst O(n²)
    Space: O(1)
    Stable: Yes, In-place: Yes
    """
    # Create a copy of the array to avoid modifying the original
    arr = arr.copy()
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr