from typing import List

def counting_sort(arr: List[int]) -> List[int]:
    """
    Counting Sort: Integer sorting using counting array
    Time: O(n + k) all cases, where k is range
    Space: O(k)
    Stable: Yes, In-place: No
    """
    # Return a copy of an empty or single-element array
    if not arr:
        return arr.copy()
    
    # Find the minimum and maximum values to determine the range
    min_val, max_val = min(arr), max(arr)
    range_size = max_val - min_val + 1
    
    # Create a count array to store the count of individual elements
    count = [0] * range_size
    output = [0] * len(arr)
    
    # Store the count of each character
    for num in arr:
        count[num - min_val] += 1
    
    # Change count[i] so that count[i] now contains the actual
    # position of this element in the output array
    for i in range(1, len(count)):
        count[i] += count[i - 1]
    
    # Build the output character array
    # To make it stable, we are operating in reverse order.
    for i in range(len(arr) - 1, -1, -1):
        output[count[arr[i] - min_val] - 1] = arr[i]
        count[arr[i] - min_val] -= 1
    
    return output