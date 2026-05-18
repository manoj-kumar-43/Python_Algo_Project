from typing import List

def heap_sort(arr: List[int]) -> List[int]:
    """
    Heap Sort: Binary heap based sorting
    Time: O(n log n) all cases
    Space: O(1)
    Stable: No, In-place: Yes
    """
    # Create a copy to sort in-place without modifying the original
    arr = arr.copy()
    n = len(arr)
    
    # Build a maxheap from the input array.
    # The range is from the last non-leaf node up to the root.
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)
    
    # One by one extract elements from the heap
    for i in range(n - 1, 0, -1):
        # Move current root (max element) to the end
        arr[0], arr[i] = arr[i], arr[0]
        # Call max heapify on the reduced heap
        heapify(arr, i, 0)
    
    return arr

def heapify(arr, n, i):
    """To heapify a subtree rooted at index i. n is size of heap."""
    largest = i  # Initialize largest as root
    left = 2 * i + 1
    right = 2 * i + 2
    
    # See if left child of root exists and is greater than root
    if left < n and arr[left] > arr[largest]:
        largest = left
        
    # See if right child of root exists and is greater than root
    if right < n and arr[right] > arr[largest]:
        largest = right
    
    # Change root, if needed
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        # Heapify the root's affected sub-tree
        heapify(arr, n, largest)