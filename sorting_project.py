"""
SORTING ALGORITHMS IMPLEMENTATION WITH MATPLOTLIB VISUALIZATION
Complete Python implementation for DAA Project

Author: [Your Name]
Date: November 2025
Course: DAA SEC-R

This file contains:
1. All 10 sorting algorithm implementations
2. Performance testing framework
3. Matplotlib visualization code
4. Complexity analysis
"""

import time
import random
import numpy as np
import matplotlib.pyplot as plt
from typing import List
import csv
import sys
import os

# Increase recursion limit for deep sorting algorithms like Quick Sort
sys.setrecursionlimit(20000)

# ============================================================================
# PART 1: SORTING ALGORITHM IMPLEMENTATIONS
# ============================================================================

# 1. BUBBLE SORT
def bubble_sort(arr: List[int]) -> List[int]:
    """
    Bubble Sort: Repeatedly swap adjacent elements if in wrong order
    Time: Best O(n), Average O(n²), Worst O(n²)
    Space: O(1)
    Stable: Yes, In-place: Yes
    """
    arr = arr.copy()
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr


# 2. SELECTION SORT
def selection_sort(arr: List[int]) -> List[int]:
    """
    Selection Sort: Find minimum and place at beginning
    Time: O(n²) all cases
    Space: O(1)
    Stable: No, In-place: Yes
    """
    arr = arr.copy()
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr


# 3. INSERTION SORT
def insertion_sort(arr: List[int]) -> List[int]:
    """
    Insertion Sort: Build sorted array one element at a time
    Time: Best O(n), Average O(n²), Worst O(n²)
    Space: O(1)
    Stable: Yes, In-place: Yes
    """
    arr = arr.copy()
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr


# 4. MERGE SORT
def merge_sort(arr: List[int]) -> List[int]:
    """
    Merge Sort: Divide and conquer sorting
    Time: O(n log n) all cases
    Space: O(n)
    Stable: Yes, In-place: No
    """
    if len(arr) <= 1:
        return arr.copy()
    
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)

def merge(left: List[int], right: List[int]) -> List[int]:
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result


# 5 & 6. QUICK SORT (Deterministic and Randomized)
def quick_sort_deterministic(arr: List[int]) -> List[int]:
    """
    Quick Sort (Deterministic): Last element as pivot
    Time: Best O(n log n), Average O(n log n), Worst O(n²)
    Space: O(log n)
    Stable: No, In-place: Yes
    """
    arr = arr.copy()
    _quick_sort_helper(arr, 0, len(arr) - 1, randomized=False)
    return arr

def quick_sort_randomized(arr: List[int]) -> List[int]:
    """
    Quick Sort (Randomized): Random element as pivot
    Time: Best O(n log n), Average O(n log n), Worst O(n²) rare
    Space: O(log n)
    Stable: No, In-place: Yes
    """
    arr = arr.copy()
    _quick_sort_helper(arr, 0, len(arr) - 1, randomized=True)
    return arr

def _quick_sort_helper(arr, low, high, randomized):
    # Iterative implementation to avoid recursion depth errors
    stack = [(low, high)]
    
    while stack:
        low, high = stack.pop()
        
        if low < high:
            pi = _partition(arr, low, high, randomized)
            
            # Push sub-problems to the stack.
            # To optimize, push the larger partition first so the stack depth
            # is determined by the smaller partition, which is O(log n) in the average case.
            if pi - low < high - pi:
                stack.append((pi + 1, high))
                stack.append((low, pi - 1))
            else:
                stack.append((low, pi - 1))
                stack.append((pi + 1, high))

def _partition(arr, low, high, randomized):
    if randomized:
        random_idx = random.randint(low, high)
        arr[random_idx], arr[high] = arr[high], arr[random_idx]
    
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


# 7. HEAP SORT
def heap_sort(arr: List[int]) -> List[int]:
    """
    Heap Sort: Binary heap based sorting
    Time: O(n log n) all cases
    Space: O(1)
    Stable: No, In-place: Yes
    """
    arr = arr.copy()
    n = len(arr)
    
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)
    
    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heapify(arr, i, 0)
    
    return arr

def heapify(arr, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2
    
    if left < n and arr[left] > arr[largest]:
        largest = left
    if right < n and arr[right] > arr[largest]:
        largest = right
    
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)


# 8. COUNTING SORT
def counting_sort(arr: List[int]) -> List[int]:
    """
    Counting Sort: Integer sorting using counting array
    Time: O(n + k) all cases, where k is range
    Space: O(k)
    Stable: Yes, In-place: No
    """
    if not arr:
        return arr.copy()
    
    min_val, max_val = min(arr), max(arr)
    range_size = max_val - min_val + 1
    
    count = [0] * range_size
    output = [0] * len(arr)
    
    for num in arr:
        count[num - min_val] += 1
    
    for i in range(1, len(count)):
        count[i] += count[i - 1]
    
    for i in range(len(arr) - 1, -1, -1):
        output[count[arr[i] - min_val] - 1] = arr[i]
        count[arr[i] - min_val] -= 1
    
    return output


# 9. RADIX SORT
def radix_sort(arr: List[int]) -> List[int]:
    """
    Radix Sort: Sort by processing digits
    Time: O(d * (n + k)) where d is number of digits
    Space: O(n + k)
    Stable: Yes, In-place: No
    """
    if not arr:
        return arr.copy()
    
    arr = arr.copy()
    min_val = min(arr)
    if min_val < 0:
        arr = [x - min_val for x in arr]
    
    max_val = max(arr)
    exp = 1
    
    while max_val // exp > 0:
        counting_sort_by_digit(arr, exp)
        exp *= 10
    
    if min_val < 0:
        arr = [x + min_val for x in arr]
    
    return arr

def counting_sort_by_digit(arr, exp):
    n = len(arr)
    output = [0] * n
    count = [0] * 10
    
    for i in range(n):
        index = (arr[i] // exp) % 10
        count[index] += 1
    
    for i in range(1, 10):
        count[i] += count[i - 1]
    
    for i in range(n - 1, -1, -1):
        index = (arr[i] // exp) % 10
        output[count[index] - 1] = arr[i]
        count[index] -= 1
    
    for i in range(n):
        arr[i] = output[i]


# 10. BUCKET SORT
def bucket_sort(arr: List[int]) -> List[int]:
    """
    Bucket Sort: Distribute into buckets and sort
    Time: Best O(n + k), Average O(n + k), Worst O(n²)
    Space: O(n + k)
    Stable: Yes, In-place: No
    """
    if not arr:
        return arr.copy()
    
    min_val, max_val = min(arr), max(arr)
    bucket_range = (max_val - min_val) / len(arr) + 1
    
    buckets = [[] for _ in range(len(arr))]
    
    for num in arr:
        index = int((num - min_val) / bucket_range)
        if index >= len(arr):
            index = len(arr) - 1
        buckets[index].append(num)
    
    result = []
    for bucket in buckets:
        result.extend(insertion_sort(bucket))
    
    return result


# ============================================================================
# PART 2: PERFORMANCE TESTING FRAMEWORK
# ============================================================================

ALGORITHMS = {
    'Bubble Sort': bubble_sort,
    'Selection Sort': selection_sort,
    'Insertion Sort': insertion_sort,
    'Merge Sort': merge_sort,
    'Quick Sort (Det)': quick_sort_deterministic,
    'Quick Sort (Rand)': quick_sort_randomized,
    'Heap Sort': heap_sort,
    'Counting Sort': counting_sort,
    'Radix Sort': radix_sort,
    'Bucket Sort': bucket_sort
}

def generate_random_data(n):
    """Generate random integer array"""
    return [random.randint(0, 10000) for _ in range(n)]

def generate_sorted_data(n):
    """Generate sorted array (best case for some algorithms)"""
    return list(range(n))

def generate_reverse_sorted_data(n):
    """Generate reverse sorted array (worst case for some algorithms)"""
    return list(range(n, 0, -1))

def measure_time(sort_func, arr, trials=3):
    """Measure average execution time over multiple trials"""
    times = []
    for _ in range(trials):
        test_arr = arr.copy()
        start = time.perf_counter()
        sort_func(test_arr)
        end = time.perf_counter()
        times.append((end - start) * 1000)  # Convert to ms
    return np.mean(times)

def run_performance_tests(input_sizes, save_csv=True):
    """
    Run comprehensive performance tests for experimental analysis
    
    Measures actual execution time using high-resolution timer (time.perf_counter())
    Tests under three input conditions:
    - Random data (average case)
    - Sorted data (best case for some algorithms)
    - Reverse sorted data (worst case for comparison-based sorts)
    
    Parameters:
    - input_sizes: list of array sizes to test
    - save_csv: whether to save results to CSV file
    
    Returns:
    - results: dictionary with performance data
    """
    results = {name: {'random': {}, 'sorted': {}, 'reverse': {}} 
               for name in ALGORITHMS.keys()}
    
    print("=" * 70)
    print("EXPERIMENTAL ANALYSIS - PERFORMANCE TESTING")
    print("=" * 70)
    
    # Efficient algorithms that can handle larger sizes
    efficient_algos = ['Merge Sort', 'Quick Sort (Det)', 'Quick Sort (Rand)', 
                       'Heap Sort', 'Counting Sort', 'Radix Sort', 'Bucket Sort']
    
    for size in input_sizes:
        print(f"\n{'=' * 70}")
        print(f"Input Size: n = {size:,}")
        print(f"{'=' * 70}")
        
        # Generate test data
        print("Generating test data...")
        random_data = generate_random_data(size)
        sorted_data = generate_sorted_data(size)
        reverse_data = generate_reverse_sorted_data(size)
        
        # Decide which algorithms to test based on size
        # O(n²) algorithms are too slow for large inputs
        algos_to_test = ALGORITHMS.keys() if size <= 5000 else efficient_algos
        
        for name in algos_to_test:
            func = ALGORITHMS[name]
            print(f"\n  {name}:")
            
            # For very large inputs, reduce trials to 1 to save time
            num_trials = 1 if size >= 100000 else 3
            
            try:
                # Test each data condition
                rand_time = measure_time(func, random_data, trials=num_trials)
                sort_time = measure_time(func, sorted_data, trials=num_trials)
                rev_time = measure_time(func, reverse_data, trials=num_trials)
                
                results[name]['random'][size] = rand_time
                results[name]['sorted'][size] = sort_time
                results[name]['reverse'][size] = rev_time
                
                print(f"    Random data:        {rand_time:>10.4f} ms")
                print(f"    Sorted data:        {sort_time:>10.4f} ms")
                print(f"    Reverse sorted:     {rev_time:>10.4f} ms")
                
            except Exception as e:
                print(f"    Error: {e}")
                results[name]['random'][size] = None
                results[name]['sorted'][size] = None
                results[name]['reverse'][size] = None
    
    # Save to CSV if requested
    if save_csv:
        save_results_to_csv(results)
    
    print("\n" + "=" * 70)
    print("EXPERIMENTAL ANALYSIS COMPLETE")
    print("=" * 70)
    print("\nSummary:")
    print(f"  - Tested {len(input_sizes)} different input sizes")
    print(f"  - Tested {len(ALGORITHMS)} sorting algorithms")
    print(f"  - Three input conditions per test (Random, Sorted, Reverse)")
    print(f"  - Used high-resolution timer (time.perf_counter())")
    print(f"  - Results saved to CSV and ready for visualization")
    
    return results

def save_results_to_csv(results):
    """Save performance results to CSV file"""
    with open('performance_results.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['Algorithm', 'Data Type', 'Size', 'Time (ms)'])
        
        for algo_name, conditions in results.items():
            for condition, size_times in conditions.items():
                for size, time_val in size_times.items():
                    if time_val is not None:
                        writer.writerow([algo_name, condition, size, f"{time_val:.4f}"])
    
    print("\n✓ Results saved to 'performance_results.csv'")


# ============================================================================
# PART 3: MATPLOTLIB VISUALIZATION
# ============================================================================

def create_all_visualizations(results):
    """Generate all matplotlib charts for the project"""
    
    print("\n" + "=" * 60)
    print("GENERATING VISUALIZATIONS")
    print("=" * 60)
    
    # Create graphs directory if it doesn't exist
    if not os.path.exists('graphs'):
        os.makedirs('graphs')
        print("✓ Created 'graphs' directory.")
        
    # Set style
    plt.style.use('seaborn-v0_8-darkgrid')
    
    # 1. Individual algorithm performance charts
    print("\n1. Creating individual algorithm charts...")
    create_individual_charts(results)
    
    # 2. Overall comparison chart
    print("2. Creating overall comparison chart...")
    create_comparison_chart(results)
    
    # 3. Complexity class comparison
    print("3. Creating complexity class comparison...")
    create_complexity_comparison(results)
    
    # 4. Bar chart for specific size
    print("4. Creating bar chart comparison...")
    create_bar_comparison(results)
    
    print("\n" + "=" * 60)
    print("ALL VISUALIZATIONS CREATED")
    print("=" * 60)

def create_individual_charts(results):
    """Create performance chart for each algorithm"""
    for algo_name, conditions in results.items():
        if not any(conditions['random'].values()):
            continue
        
        plt.figure(figsize=(10, 6))
        
        sizes = sorted(conditions['random'].keys())
        random_times = [conditions['random'][s] for s in sizes]
        sorted_times = [conditions['sorted'][s] for s in sizes]
        reverse_times = [conditions['reverse'][s] for s in sizes]
        
        plt.plot(sizes, random_times, 'o-', label='Random Data', linewidth=2)
        plt.plot(sizes, sorted_times, 's-', label='Sorted Data', linewidth=2)
        plt.plot(sizes, reverse_times, '^-', label='Reverse Sorted', linewidth=2)
        
        # --- START: Added Theoretical Curve ---
        
        complexity_map = {
            'Bubble Sort': 'O(n^2)', 'Selection Sort': 'O(n^2)', 'Insertion Sort': 'O(n^2)',
            'Merge Sort': 'O(n log n)', 'Quick Sort (Det)': 'O(n log n)', 
            'Quick Sort (Rand)': 'O(n log n)', 'Heap Sort': 'O(n log n)',
            'Counting Sort': 'O(n)', 'Radix Sort': 'O(n)', 'Bucket Sort': 'O(n)'
        }
        
        complexity = complexity_map.get(algo_name)
        
        if complexity and len(sizes) > 1:
            # Find the last valid data point to scale the theoretical curve
            last_size = None
            last_time = None
            for i in range(len(sizes) - 1, -1, -1):
                if random_times[i] is not None:
                    last_size = sizes[i]
                    last_time = random_times[i]
                    break

            if last_time is not None and last_size is not None:
                n_range = np.linspace(sizes[0], sizes[-1], 200)
                theoretical_curve = None
                
                if complexity == 'O(n^2)' and last_size > 0:
                    # c * n^2 = time -> c = time / n^2
                    c = last_time / (last_size ** 2)
                    theoretical_curve = c * (n_range ** 2)
                elif complexity == 'O(n log n)' and last_size > 1:
                    # c * n * log(n) = time -> c = time / (n * log(n))
                    # Add a small epsilon to avoid log2(1) = 0 issues
                    c = last_time / (last_size * np.log2(last_size + 1e-9))
                    theoretical_curve = c * n_range * np.log2(n_range + 1e-9)
                elif complexity == 'O(n)' and last_size > 0:
                    # c * n = time -> c = time / n
                    c = last_time / last_size
                    theoretical_curve = c * n_range

                if theoretical_curve is not None:
                    plt.plot(n_range, theoretical_curve, 'r--', 
                             label=f'Theoretical Trend ({complexity})', linewidth=2)

        # --- END: Added Theoretical Curve ---
        
        plt.xlabel('Input Size (n)', fontsize=12, fontweight='bold')
        plt.ylabel('Time (milliseconds)', fontsize=12, fontweight='bold')
        plt.title(f'{algo_name} - Performance Analysis', fontsize=14, fontweight='bold')
        plt.legend(fontsize=10)
        plt.grid(True, alpha=0.3)
        plt.tight_layout()
        
        filename = f'graphs/{algo_name.replace(" ", "_").replace("(", "").replace(")", "")}_performance.png'
        plt.savefig(filename, dpi=300)
        plt.close()
        print(f"   ✓ {filename}")

def create_comparison_chart(results):
    """Create overall comparison chart with all algorithms"""
    plt.figure(figsize=(12, 8))
    
    for algo_name, conditions in results.items():
        if not any(conditions['random'].values()):
            continue
        
        sizes = sorted(conditions['random'].keys())
        times = [conditions['random'][s] for s in sizes]
        
        plt.plot(sizes, times, 'o-', label=algo_name, linewidth=2, markersize=6)
    
    plt.xlabel('Input Size (n)', fontsize=12, fontweight='bold')
    plt.ylabel('Time (milliseconds) - Log Scale', fontsize=12, fontweight='bold')
    plt.title('Sorting Algorithms - Overall Performance Comparison', 
              fontsize=14, fontweight='bold')
    plt.legend(fontsize=9, loc='upper left')
    plt.grid(True, alpha=0.3)
    plt.yscale('log')
    plt.tight_layout()
    plt.savefig('graphs/comparison_all_algorithms.png', dpi=300)
    plt.close()
    print("   ✓ graphs/comparison_all_algorithms.png")

def create_complexity_comparison(results):
    """Compare algorithms by complexity class"""
    fig, axes = plt.subplots(1, 3, figsize=(18, 5))
    
    # O(n²) algorithms
    on2_algos = ['Bubble Sort', 'Selection Sort', 'Insertion Sort']
    for algo in on2_algos:
        if algo in results and any(results[algo]['random'].values()):
            sizes = sorted(results[algo]['random'].keys())
            times = [results[algo]['random'][s] for s in sizes]
            axes[0].plot(sizes, times, 'o-', label=algo, linewidth=2)
    
    axes[0].set_xlabel('Input Size (n)', fontweight='bold')
    axes[0].set_ylabel('Time (ms)', fontweight='bold')
    axes[0].set_title('O(n²) Algorithms', fontweight='bold', fontsize=12)
    axes[0].legend()
    axes[0].grid(True, alpha=0.3)
    
    # O(n log n) algorithms
    onlogn_algos = ['Merge Sort', 'Quick Sort (Det)', 'Quick Sort (Rand)', 'Heap Sort']
    for algo in onlogn_algos:
        if algo in results and any(results[algo]['random'].values()):
            sizes = sorted(results[algo]['random'].keys())
            times = [results[algo]['random'][s] for s in sizes]
            axes[1].plot(sizes, times, 's-', label=algo, linewidth=2)
    
    axes[1].set_xlabel('Input Size (n)', fontweight='bold')
    axes[1].set_ylabel('Time (ms)', fontweight='bold')
    axes[1].set_title('O(n log n) Algorithms', fontweight='bold', fontsize=12)
    axes[1].legend()
    axes[1].grid(True, alpha=0.3)
    
    # Linear time algorithms
    linear_algos = ['Counting Sort', 'Radix Sort', 'Bucket Sort']
    for algo in linear_algos:
        if algo in results and any(results[algo]['random'].values()):
            sizes = sorted(results[algo]['random'].keys())
            times = [results[algo]['random'][s] for s in sizes]
            axes[2].plot(sizes, times, '^-', label=algo, linewidth=2)
    
    axes[2].set_xlabel('Input Size (n)', fontweight='bold')
    axes[2].set_ylabel('Time (ms)', fontweight='bold')
    axes[2].set_title('O(n+k) / O(d(n+k)) Algorithms', fontweight='bold', fontsize=12)
    axes[2].legend()
    axes[2].grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.savefig('graphs/comparison_by_complexity.png', dpi=300)
    plt.close()
    print("   ✓ graphs/comparison_by_complexity.png")

def create_bar_comparison(results, size=1000):
    """Create bar chart for specific input size"""
    algo_names = []
    times = []
    
    for algo, conditions in results.items():
        if size in conditions['random'] and conditions['random'][size] is not None:
            algo_names.append(algo)
            times.append(conditions['random'][size])
    
    plt.figure(figsize=(12, 6))
    bars = plt.bar(range(len(algo_names)), times, color='steelblue', 
                   edgecolor='black', alpha=0.7)
    plt.xticks(range(len(algo_names)), algo_names, rotation=45, ha='right')
    plt.ylabel('Time (milliseconds)', fontsize=12, fontweight='bold')
    plt.title(f'Algorithm Performance Comparison (n={size}, Random Data)', 
              fontsize=14, fontweight='bold')
    plt.grid(axis='y', alpha=0.3)
    plt.tight_layout()
    plt.savefig(f'graphs/bar_comparison_n{size}.png', dpi=300)
    plt.close()
    print(f"   ✓ graphs/bar_comparison_n{size}.png")


# =========================================================================
# ============================================================================

def main():
    """Main execution function"""
    print("\n" + "=" * 60)
    print("SORTING ALGORITHMS - COMPARATIVE STUDY")
    print("DAA Project Assignment")
    print("=" * 60)
    
    # Test correctness first
    print("\n1. Testing algorithm correctness...")
    test_array = [64, 34, 25, 12, 22, 11, 90]
    expected = sorted(test_array)
    
    all_correct = True
    for name, func in ALGORITHMS.items():
        result = func(test_array)
        if result == expected:
            print(f"   ✓ {name}")
        else:
            print(f"   ✗ {name} FAILED")
            all_correct = False
    
    if not all_correct:
        print("\n⚠ Some algorithms failed. Please check implementations.")
        return
    
    print("\n✓ All algorithms passed correctness tests!")
    
    # Define input sizes for testing (as per project requirements)
    # Use smaller sizes for O(n²) algorithms and larger for efficient algorithms
    input_sizes = [100, 1000, 2000, 3000, 4000, 5000, 10000, 15000, 20000]
    
    print("\n2. Running experimental analysis...")
    print("   Input sizes:", input_sizes)
    print("   Test conditions:")
    print("     - Random data (average case)")
    print("     - Sorted data (best case)")
    print("     - Reverse sorted data (worst case)")
    print("   Using high-resolution performance counter (time.perf_counter())")
    
    # Run performance tests
    results = run_performance_tests(input_sizes, save_csv=True)
    
    # Create visualizations
    print("\n3. Creating visualizations...")
    create_all_visualizations(results)
    
    # Print summary
    print("\n" + "=" * 60)
    print("PROJECT COMPLETE!")
    print("=" * 60)
    print("\nGenerated Files:")
    print("  - performance_results.csv (performance data)")
    print("  - All charts are in the 'graphs/' directory")
    print("\nNext Steps:")
    print("  1. Review the generated charts")
    print("  2. Analyze the performance data in CSV")
    print("  3. Write your report with observations")
    print("  4. Prepare for viva with complexity explanations")

if __name__ == "__main__":
    main()
