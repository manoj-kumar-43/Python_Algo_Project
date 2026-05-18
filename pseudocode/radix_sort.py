from typing import List

def radix_sort(arr: List[int]) -> List[int]:
    """
    Radix Sort: Sort by processing digits
    Time: O(d * (n + k)) where d is number of digits
    Space: O(n + k)
    Stable: Yes, In-place: No
    """
    if not arr:
        return arr.copy()
    
    # Create a copy to avoid modifying the original array
    arr = arr.copy()
    
    # Handle negative numbers by shifting all numbers to be non-negative
    min_val = min(arr)
    if min_val < 0:
        arr = [x - min_val for x in arr]
    
    # Find the maximum number to know number of digits
    max_val = max(arr)
    
    # Do counting sort for every digit. Note that instead of passing digit
    # number, exp is passed. exp is 10^i where i is current digit number.
    exp = 1
    while max_val // exp > 0:
        counting_sort_by_digit(arr, exp)
        exp *= 10
    
    # Shift the numbers back if they were originally negative
    if min_val < 0:
        arr = [x + min_val for x in arr]
    
    return arr

def counting_sort_by_digit(arr, exp):
    """A helper function to do counting sort of arr[] according to the digit represented by exp."""
    n = len(arr)
    output = [0] * n  # output array
    count = [0] * 10  # count array for digits 0-9
    
    # Store count of occurrences in count[]
    for i in range(n):
        index = (arr[i] // exp) % 10
        count[index] += 1
    
    # Change count[i] so that count[i] now contains actual
    # position of this digit in output[]
    for i in range(1, 10):
        count[i] += count[i - 1]
    
    # Build the output array
    for i in range(n - 1, -1, -1):
        index = (arr[i] // exp) % 10
        output[count[index] - 1] = arr[i]
        count[index] -= 1
    
    # Copy the output array to arr[], so that arr[] now
    # contains sorted numbers according to current digit
    for i in range(n):
        arr[i] = output[i]