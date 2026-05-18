# Sorting Algorithms - Comparative Study

**Design and Analysis of Algorithms (DAA) Project**  
**Course:** DAA SEC-R  
**Date:** November 2025

---

## 📋 Project Overview

This project presents a comprehensive comparative analysis of **10 fundamental sorting algorithms**, combining theoretical complexity analysis with extensive experimental performance testing. The project implements each algorithm from scratch in Python, performs rigorous testing across multiple input conditions, and generates professional visualizations to demonstrate performance characteristics.

### Algorithms Covered

1. **Bubble Sort** - Simple comparison-based algorithm
2. **Selection Sort** - In-place comparison sort
3. **Insertion Sort** - Efficient for small/nearly sorted data
4. **Merge Sort** - Divide-and-conquer approach
5. **Quick Sort (Deterministic)** - Efficient in-place sorting
6. **Quick Sort (Randomized)** - Randomized pivot selection
7. **Heap Sort** - Heap-based selection sort
8. **Counting Sort** - Integer sorting (non-comparison)
9. **Radix Sort** - Digit-by-digit sorting
10. **Bucket Sort** - Distribution-based sorting

---

## 📁 Project Structure

```
classwork/
│
├── README.md                                    # This file - project documentation
│
├── sorting_project.py                           # Main implementation file (741 lines)
│   ├── All 10 sorting algorithms
│   ├── Performance testing framework
│   ├── Data generation (random, sorted, reverse)
│   ├── Timing measurements with perf_counter
│   └── CSV output generation
│
├── generate_individual_algorithm_graphs.py      # Visualization script (351 lines)
│   ├── Individual algorithm graphs
│   ├── Comparison graphs by input size
│   ├── Scaling analysis (log-log plots)
│   ├── Case analysis (best/average/worst)
│   └── Speedup comparison charts
│
├── experimental_analysis.txt                    # Raw experimental results
│   ├── Correctness test results
│   ├── Performance data for all algorithms
│   ├── Multiple input sizes (100 to 10M elements)
│   └── Three test conditions per algorithm
│
├── experimental_analytics.tex                   # LaTeX report (200 lines)
│   ├── Formatted experimental results
│   ├── Performance tables
│   ├── Graph inclusions
│   └── Analysis and observations
│
├── Theoretical_Complexity.tex                   # LaTeX theory document (214 lines)
│   ├── Time complexity analysis table
│   ├── Space complexity analysis
│   ├── Stability and in-place properties
│   └── Theoretical comparisons
│
├── viva_questions.md                            # Exam preparation (591 lines)
│   ├── 50+ comprehensive viva questions
│   ├── Fundamental concepts
│   ├── Algorithm-specific questions
│   ├── Complexity analysis questions
│   └── Practical implementation insights
│
├── matplotlib_guide.md                          # Visualization guidelines
│   └── Matplotlib best practices for graphs
│
├── graphs/                                      # Generated visualizations directory
│   ├── GRAPHS_SUMMARY.md                        # Documentation of all graphs
│   ├── comparison_1000.png                      # Performance at 1K elements
│   ├── comparison_10000.png                     # Performance at 10K elements
│   ├── comparison_1000000.png                   # Performance at 1M elements
│   ├── scaling_all_algorithms.png               # All algorithms scaling (log-log)
│   ├── efficient_algorithms_comparison.png      # O(n log n) algorithms
│   ├── linear_algorithms_comparison.png         # O(n) algorithms
│   ├── bubble_sort_cases.png                    # Best/avg/worst case analysis
│   ├── insertion_sort_cases.png                 # Best/avg/worst case analysis
│   ├── quick_sort_rand_cases.png                # Best/avg/worst case analysis
│   ├── merge_sort_cases.png                     # Best/avg/worst case analysis
│   ├── speedup_comparison.png                   # Speedup factors visualization
│   └── [10 individual algorithm graphs]         # One per algorithm
│
└── pseudocode/                                  # Clean algorithm implementations
    ├── bubble_sort.py                           # Bubble sort with comments
    ├── selection_sort.py                        # Selection sort with comments
    ├── insertion_sort.py                        # Insertion sort with comments
    ├── merge_sort.py                            # Merge sort with comments
    ├── quick_sort_deterministic.py              # Quick sort (deterministic)
    ├── quick_sort_randomized.py                 # Quick sort (randomized)
    ├── heap_sort.py                             # Heap sort with comments
    ├── counting_sort.py                         # Counting sort with comments
    ├── radix_sort.py                            # Radix sort with comments
    └── bucket_sort.py                           # Bucket sort with comments
```

---

## 🚀 Quick Start

### Prerequisites

```bash
# Python 3.8 or higher
python3 --version

# Required packages
pip install numpy matplotlib
```

### Running the Analysis

```bash
# Run complete experimental analysis
python3 sorting_project.py

# Generate all visualization graphs
python3 generate_individual_algorithm_graphs.py

# Compile LaTeX documents (requires LaTeX distribution)
pdflatex experimental_analytics.tex
pdflatex Theoretical_Complexity.tex
```

---

## 📊 Experimental Methodology

### Test Configuration

- **Input Sizes:** 100, 500, 1K, 5K, 10K, 50K, 100K, 500K, 1M, 5M, 10M elements
- **Data Conditions:**
  - **Random Data** (Average Case)
  - **Sorted Data** (Best Case)
  - **Reverse Sorted Data** (Worst Case)
- **Timing Method:** `time.perf_counter()` for high-resolution measurements
- **Repetitions:** Multiple runs to ensure consistency

### Algorithm Correctness Testing

Each algorithm is validated against:
- Small test cases (sorted, reverse, duplicates)
- Medium-sized random arrays
- Edge cases (empty, single element)

---

## 📈 Key Findings

### Performance Highlights

| Algorithm | Best Case | Average Case | Worst Case | Stable |
|-----------|-----------|--------------|------------|--------|
| Bubble Sort | O(n) | O(n²) | O(n²) | Yes |
| Selection Sort | O(n²) | O(n²) | O(n²) | No |
| Insertion Sort | O(n) | O(n²) | O(n²) | Yes |
| Merge Sort | O(n log n) | O(n log n) | O(n log n) | Yes |
| Quick Sort (Det) | O(n log n) | O(n log n) | O(n²) | No |
| Quick Sort (Rand) | O(n log n) | O(n log n) | O(n²)* | No |
| Heap Sort | O(n log n) | O(n log n) | O(n log n) | No |
| Counting Sort | O(n+k) | O(n+k) | O(n+k) | Yes |
| Radix Sort | O(d·n) | O(d·n) | O(d·n) | Yes |
| Bucket Sort | O(n) | O(n+k) | O(n²) | Yes |

*Extremely unlikely with randomization

### Speedup Factors (Best vs Worst Case)

- **Bubble Sort:** 5,520x speedup (sorted vs reverse sorted at n=5,000)
- **Insertion Sort:** 2,018x speedup (sorted vs reverse sorted at n=5,000)
- **Quick Sort (Randomized):** Consistent performance across all cases

### Algorithm Recommendations

- **Small datasets (n < 100):** Insertion Sort
- **Medium datasets (n < 10K):** Quick Sort (Randomized)
- **Large datasets (n > 10K):** Merge Sort or Quick Sort
- **Nearly sorted data:** Insertion Sort or Bubble Sort (optimized)
- **Integer data with small range:** Counting Sort or Radix Sort
- **Guaranteed O(n log n):** Merge Sort or Heap Sort

---

## 📚 Documentation Files

### 1. `experimental_analytics.tex`
Professional LaTeX report containing:
- Formatted performance tables
- All generated graphs
- Statistical analysis
- Observations and conclusions

### 2. `Theoretical_Complexity.tex`
Theoretical analysis including:
- Time complexity derivations
- Space complexity analysis
- Recurrence relations
- Mathematical proofs

### 3. `viva_questions.md`
Comprehensive exam preparation with:
- 50+ viva questions and answers
- Conceptual understanding
- Algorithm-specific questions
- Complexity analysis explanations
- Real-world application scenarios

---

## 🔬 Visualization Categories

### Category 1: Size-Specific Comparisons (3 graphs)
Compare all algorithms at specific input sizes with different data conditions

### Category 2: Scaling Analysis (3 graphs)
Show how algorithms scale across all input sizes using log-log plots

### Category 3: Case Analysis (4 graphs)
Best vs Average vs Worst case performance for key algorithms

### Category 4: Special Analysis (2 graphs)
Speedup comparisons and additional insights

### Category 5: Individual Algorithm Graphs (10 graphs)
Each algorithm with theoretical curve overlaid on experimental data points

---

## 💻 Code Organization

### `sorting_project.py`
**Main Sections:**
1. Algorithm implementations (10 functions)
2. Helper functions (merge, partition, heapify, etc.)
3. Data generation utilities
4. Performance testing framework
5. Output formatting and CSV export

### `generate_individual_algorithm_graphs.py`
**Features:**
- Matplotlib configuration for professional output
- Experimental data arrays
- Theoretical complexity curves
- Multiple graph types (line, bar, scatter)
- High-resolution PNG export (300 DPI)

### `pseudocode/` Directory
Clean, well-commented implementations of each algorithm for educational purposes and easy reference.

---

## 🎯 Learning Objectives Achieved

✅ **Implementation:** All 10 sorting algorithms coded from scratch  
✅ **Analysis:** Theoretical complexity analysis completed  
✅ **Experimentation:** Extensive performance testing conducted  
✅ **Visualization:** 22+ professional graphs generated  
✅ **Documentation:** Comprehensive LaTeX reports prepared  
✅ **Understanding:** Viva questions document created  

---

## 📝 Notes

- **Recursion Limit:** Set to 20,000 in `sorting_project.py` for deep recursion in Quick Sort
- **Memory Considerations:** Large input sizes (5M, 10M) may require significant RAM
- **Graph Resolution:** All graphs saved at 300 DPI for publication quality
- **LaTeX Compilation:** Requires full TeX distribution (TeX Live or MiKTeX)

---

## 🔄 Reproducibility

All results in this project are fully reproducible:
1. Run `sorting_project.py` to regenerate experimental data
2. Run `generate_individual_algorithm_graphs.py` to regenerate all graphs
3. Compile LaTeX files to regenerate PDF reports

---

## 📧 Project Information

**Repository:** DAA-Project  
**Owner:** lviffy  
**Branch:** main  
**Date:** November 2025  

---

## 🙏 Acknowledgments

This project demonstrates the practical application of algorithm analysis concepts covered in the Design and Analysis of Algorithms course, combining theoretical foundations with empirical validation.

---

## 📖 Usage Examples

### Running Individual Algorithms

```python
from sorting_project import merge_sort, quick_sort_randomized

# Sort an array
arr = [64, 34, 25, 12, 22, 11, 90]
sorted_arr = merge_sort(arr)
print(sorted_arr)  # [11, 12, 22, 25, 34, 64, 90]
```

### Accessing Pseudocode

```python
# Import clean implementations
from pseudocode.merge_sort import merge_sort
from pseudocode.quick_sort_randomized import quick_sort_randomized

# Use for learning or testing
result = merge_sort([5, 2, 8, 1, 9])
```

---

**End of README**
