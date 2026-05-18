# HOW TO CREATE MATPLOTLIB VISUALIZATIONS FOR YOUR DAA PROJECT

## Complete Guide to Generating Performance Graphs

This guide provides detailed step-by-step instructions for creating professional Matplotlib visualizations to accompany your DAA sorting algorithms project report.

---

## SETUP: Install Required Libraries

Before starting, ensure you have the necessary packages installed:

```bash
pip install matplotlib numpy
```

If you also have the performance data:
```bash
pip install pandas
```

---

## METHOD 1: CREATING INDIVIDUAL ALGORITHM CHARTS (1 per algorithm)

Each algorithm should have one chart showing performance under three conditions: Random Data, Sorted Data, and Reverse-Sorted Data.

### Step 1: Prepare Your Data

First, create a Python file `plot_algorithms.py` and organize your performance data:

```python
import matplotlib.pyplot as plt
import numpy as np

# Define input sizes
input_sizes = [100, 500, 1000, 2500, 5000, 10000]

# Performance data for each algorithm
# Format: {algorithm_name: [times in ms for random, sorted, reverse]}
performance_data = {
    'Bubble Sort': {
        'random': [1.2, 29.9, 120, 745, 3000, 12000],
        'sorted': [0.12, 0.30, 0.60, 3.0, 6.0, 12.0],
        'reverse': [1.3, 31.5, 126, 3150, 12600, 25200]
    },
    'Selection Sort': {
        'random': [1.0, 25.0, 100, 620, 2500, 10000],
        'sorted': [1.0, 25.0, 100, 620, 2500, 10000],
        'reverse': [1.0, 25.0, 100, 620, 2500, 10000]
    },
    'Insertion Sort': {
        'random': [0.8, 20.0, 80, 495, 2000, 8000],
        'sorted': [0.05, 0.10, 0.20, 1.0, 2.0, 4.0],
        'reverse': [1.2, 24.5, 98, 2450, 9800, 19600]
    },
    'Merge Sort': {
        'random': [0.66, 4.48, 9.97, 31.0, 61.4, 132.9],
        'sorted': [0.63, 4.20, 9.50, 29.5, 59.0, 127.0],
        'reverse': [0.68, 4.56, 10.15, 31.7, 63.4, 136.8]
    },
    'Quick Sort': {
        'random': [0.59, 3.98, 8.46, 26.5, 51.4, 113.0],
        'sorted': [0.45, 2.88, 6.20, 18.6, 40.0, 92.0],
        'reverse': [0.95, 5.95, 12.8, 39.6, 93.0, 215.0]
    },
    'Heap Sort': {
        'random': [0.79, 5.37, 11.51, 35.8, 69.3, 149.5],
        'sorted': [0.75, 5.1, 11.0, 34.0, 67.0, 145.0],
        'reverse': [0.82, 5.45, 11.75, 36.4, 70.5, 152.0]
    },
    'Counting Sort': {
        'random': [0.15, 0.75, 1.5, 3.75, 7.5, 15.0],
        'sorted': [0.15, 0.73, 1.48, 3.7, 7.4, 14.8],
        'reverse': [0.16, 0.76, 1.52, 3.8, 7.6, 15.2]
    }
}
```

### Step 2: Create Individual Chart Function

Add this function to plot each algorithm:

```python
def plot_individual_algorithm(algo_name, sizes, random_times, sorted_times, reverse_times):
    """
    Create a chart for a single algorithm showing performance under three conditions.
    
    Parameters:
    - algo_name: Name of the algorithm
    - sizes: List of input sizes
    - random_times: Times for random data
    - sorted_times: Times for sorted data  
    - reverse_times: Times for reverse-sorted data
    """
    plt.figure(figsize=(10, 6))
    
    # Plot three lines for different data conditions
    plt.plot(sizes, random_times, 'o-', label='Random Data', linewidth=2.5, markersize=8, color='#1f77b4')
    plt.plot(sizes, sorted_times, 's-', label='Sorted Data (Best Case)', linewidth=2.5, markersize=8, color='#2ca02c')
    plt.plot(sizes, reverse_times, '^-', label='Reverse Sorted (Worst Case)', linewidth=2.5, markersize=8, color='#d62728')
    
    # Customize labels and title
    plt.xlabel('Input Size (n)', fontsize=12, fontweight='bold')
    plt.ylabel('Time (milliseconds)', fontsize=12, fontweight='bold')
    plt.title(f'{algo_name} - Performance Analysis', fontsize=14, fontweight='bold')
    
    # Add legend and grid
    plt.legend(fontsize=10, loc='upper left')
    plt.grid(True, alpha=0.3, linestyle='--')
    
    # Format axes
    plt.tight_layout()
    
    # Save the figure
    filename = f'{algo_name.replace(" ", "_")}_performance.png'
    plt.savefig(filename, dpi=300, bbox_inches='tight')
    print(f"✓ Saved: {filename}")
    
    plt.close()  # Close to avoid memory issues
```

### Step 3: Generate All Individual Charts

```python
# Generate individual chart for each algorithm
for algo_name, data in performance_data.items():
    plot_individual_algorithm(
        algo_name,
        input_sizes,
        data['random'],
        data['sorted'],
        data['reverse']
    )

print("\n✓ All individual algorithm charts created!")
```

---

## METHOD 2: CREATING OVERALL COMPARISON CHART

This chart compares all algorithms on a single graph to visualize relative performance.

```python
def plot_all_algorithms_comparison():
    """
    Create a comprehensive comparison chart for all algorithms on random data.
    Uses logarithmic Y-axis to show differences across orders of magnitude.
    """
    plt.figure(figsize=(14, 8))
    
    # Define colors for different algorithms
    colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b', '#e377c2']
    line_styles = ['-', '-', '-', '-', '-', '-', '-']
    markers = ['o', 's', '^', 'D', 'v', '<', '>']
    
    # Plot each algorithm
    for (algo_name, data), color, marker in zip(performance_data.items(), colors, markers):
        plt.plot(input_sizes, data['random'], marker=marker, label=algo_name, 
                linewidth=2.5, markersize=7, color=color, linestyle='-', alpha=0.8)
    
    # Customize the plot
    plt.xlabel('Input Size (n)', fontsize=12, fontweight='bold')
    plt.ylabel('Time (milliseconds) - Log Scale', fontsize=12, fontweight='bold')
    plt.title('Sorting Algorithms - Overall Performance Comparison (Random Data)', 
              fontsize=14, fontweight='bold')
    
    # Use logarithmic scale on Y-axis
    plt.yscale('log')
    
    # Add legend
    plt.legend(fontsize=10, loc='upper left', framealpha=0.95)
    
    # Add grid
    plt.grid(True, which='both', alpha=0.3, linestyle='--')
    
    plt.tight_layout()
    plt.savefig('comparison_all_algorithms.png', dpi=300, bbox_inches='tight')
    print("✓ Saved: comparison_all_algorithms.png")
    plt.close()
```

### Call the function:

```python
plot_all_algorithms_comparison()
```

---

## METHOD 3: CREATING COMPLEXITY CLASS COMPARISON

This creates three subplots comparing algorithms grouped by complexity class.

```python
def plot_complexity_class_comparison():
    """
    Create three subplots showing algorithms grouped by complexity class:
    - O(n²) algorithms
    - O(n log n) algorithms
    - Linear time algorithms
    """
    fig, axes = plt.subplots(1, 3, figsize=(18, 6))
    
    # O(n²) Algorithms
    on2_algorithms = {
        'Bubble Sort': performance_data['Bubble Sort']['random'],
        'Selection Sort': performance_data['Selection Sort']['random'],
        'Insertion Sort': performance_data['Insertion Sort']['random']
    }
    
    for algo, times in on2_algorithms.items():
        axes[0].plot(input_sizes, times, 'o-', label=algo, linewidth=2.5, markersize=7)
    
    axes[0].set_xlabel('Input Size (n)', fontsize=11, fontweight='bold')
    axes[0].set_ylabel('Time (ms)', fontsize=11, fontweight='bold')
    axes[0].set_title('O(n²) Algorithms', fontsize=12, fontweight='bold')
    axes[0].legend(fontsize=9)
    axes[0].grid(True, alpha=0.3)
    axes[0].set_yscale('log')
    
    # O(n log n) Algorithms
    onlogn_algorithms = {
        'Merge Sort': performance_data['Merge Sort']['random'],
        'Quick Sort': performance_data['Quick Sort']['random'],
        'Heap Sort': performance_data['Heap Sort']['random']
    }
    
    for algo, times in onlogn_algorithms.items():
        axes[1].plot(input_sizes, times, 's-', label=algo, linewidth=2.5, markersize=7)
    
    axes[1].set_xlabel('Input Size (n)', fontsize=11, fontweight='bold')
    axes[1].set_ylabel('Time (ms)', fontsize=11, fontweight='bold')
    axes[1].set_title('O(n log n) Algorithms', fontsize=12, fontweight='bold')
    axes[1].legend(fontsize=9)
    axes[1].grid(True, alpha=0.3)
    
    # Linear Time Algorithms
    linear_algorithms = {
        'Counting Sort': performance_data['Counting Sort']['random']
    }
    
    for algo, times in linear_algorithms.items():
        axes[2].plot(input_sizes, times, '^-', label=algo, linewidth=2.5, markersize=7, color='#2ca02c')
    
    axes[2].set_xlabel('Input Size (n)', fontsize=11, fontweight='bold')
    axes[2].set_ylabel('Time (ms)', fontsize=11, fontweight='bold')
    axes[2].set_title('O(n + k) Algorithms', fontsize=12, fontweight='bold')
    axes[2].legend(fontsize=9)
    axes[2].grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.savefig('comparison_by_complexity.png', dpi=300, bbox_inches='tight')
    print("✓ Saved: comparison_by_complexity.png")
    plt.close()

plot_complexity_class_comparison()
```

---

## METHOD 4: CREATING BAR CHART COMPARISON

Compare all algorithms at a specific input size using a bar chart.

```python
def plot_bar_comparison(size=1000):
    """
    Create a bar chart comparing algorithm performance at a specific input size.
    
    Parameters:
    - size: The input size to compare (should be in input_sizes list)
    """
    # Find the index of the selected size
    size_idx = input_sizes.index(size)
    
    # Extract times for the selected size
    algo_names = []
    times = []
    
    for algo_name, data in performance_data.items():
        algo_names.append(algo_name)
        times.append(data['random'][size_idx])
    
    # Create bar chart
    fig, ax = plt.subplots(figsize=(12, 6))
    
    # Define colors based on algorithm type
    colors = []
    for algo in algo_names:
        if algo in ['Bubble Sort', 'Selection Sort', 'Insertion Sort']:
            colors.append('#FF6B6B')  # Red for O(n²)
        elif algo in ['Counting Sort']:
            colors.append('#51CF66')  # Green for O(n+k)
        else:
            colors.append('#4ECDC4')  # Teal for O(n log n)
    
    # Create bars
    bars = ax.bar(range(len(algo_names)), times, color=colors, edgecolor='black', alpha=0.7)
    
    # Add value labels on top of bars
    for i, (bar, time) in enumerate(zip(bars, times)):
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2., height,
                f'{time:.2f}ms',
                ha='center', va='bottom', fontsize=9, fontweight='bold')
    
    # Customize plot
    ax.set_xticks(range(len(algo_names)))
    ax.set_xticklabels(algo_names, rotation=45, ha='right')
    ax.set_ylabel('Time (milliseconds)', fontsize=12, fontweight='bold')
    ax.set_title(f'Algorithm Performance Comparison (n={size}, Random Data)', 
                 fontsize=14, fontweight='bold')
    ax.grid(axis='y', alpha=0.3, linestyle='--')
    
    plt.tight_layout()
    plt.savefig(f'bar_comparison_n{size}.png', dpi=300, bbox_inches='tight')
    print(f"✓ Saved: bar_comparison_n{size}.png")
    plt.close()

# Generate bar chart for n=1000
plot_bar_comparison(1000)
```

---

## METHOD 5: CREATING BEST VS WORST CASE COMPARISON

Compare best-case and worst-case performance for an algorithm.

```python
def plot_best_vs_worst_case(algo_name):
    """
    Create a comparison chart for best-case vs worst-case performance.
    
    Parameters:
    - algo_name: Name of the algorithm to compare
    """
    if algo_name not in performance_data:
        print(f"Algorithm '{algo_name}' not found!")
        return
    
    data = performance_data[algo_name]
    
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5))
    
    # Left plot: Best case (sorted data)
    ax1.plot(input_sizes, data['sorted'], 'o-', linewidth=2.5, markersize=8, 
            color='#2ca02c', label='Sorted (Best)')
    ax1.fill_between(input_sizes, data['sorted'], alpha=0.3, color='#2ca02c')
    ax1.set_xlabel('Input Size (n)', fontsize=11, fontweight='bold')
    ax1.set_ylabel('Time (milliseconds)', fontsize=11, fontweight='bold')
    ax1.set_title(f'{algo_name} - Best Case (Sorted Data)', fontsize=12, fontweight='bold')
    ax1.grid(True, alpha=0.3)
    ax1.set_yscale('log')
    
    # Right plot: Worst case (reverse sorted)
    ax2.plot(input_sizes, data['reverse'], '^-', linewidth=2.5, markersize=8, 
            color='#d62728', label='Reverse Sorted (Worst)')
    ax2.fill_between(input_sizes, data['reverse'], alpha=0.3, color='#d62728')
    ax2.set_xlabel('Input Size (n)', fontsize=11, fontweight='bold')
    ax2.set_ylabel('Time (milliseconds)', fontsize=11, fontweight='bold')
    ax2.set_title(f'{algo_name} - Worst Case (Reverse Sorted)', fontsize=12, fontweight='bold')
    ax2.grid(True, alpha=0.3)
    ax2.set_yscale('log')
    
    plt.tight_layout()
    plt.savefig(f'{algo_name.replace(" ", "_")}_best_vs_worst.png', dpi=300, bbox_inches='tight')
    print(f"✓ Saved: {algo_name.replace(' ', '_')}_best_vs_worst.png")
    plt.close()

# Create best vs worst comparison for Quick Sort
plot_best_vs_worst_case('Quick Sort')
```

---

## METHOD 6: COMPLETE SCRIPT - RUN ALL VISUALIZATIONS

Create a file `generate_all_plots.py` and paste this complete script:

```python
import matplotlib.pyplot as plt
import numpy as np

# Set style for professional appearance
plt.style.use('seaborn-v0_8-darkgrid')

# Define input sizes
input_sizes = [100, 500, 1000, 2500, 5000, 10000]

# Performance data
performance_data = {
    'Bubble Sort': {
        'random': [1.2, 29.9, 120, 745, 3000, 12000],
        'sorted': [0.12, 0.30, 0.60, 3.0, 6.0, 12.0],
        'reverse': [1.3, 31.5, 126, 3150, 12600, 25200]
    },
    'Selection Sort': {
        'random': [1.0, 25.0, 100, 620, 2500, 10000],
        'sorted': [1.0, 25.0, 100, 620, 2500, 10000],
        'reverse': [1.0, 25.0, 100, 620, 2500, 10000]
    },
    'Insertion Sort': {
        'random': [0.8, 20.0, 80, 495, 2000, 8000],
        'sorted': [0.05, 0.10, 0.20, 1.0, 2.0, 4.0],
        'reverse': [1.2, 24.5, 98, 2450, 9800, 19600]
    },
    'Merge Sort': {
        'random': [0.66, 4.48, 9.97, 31.0, 61.4, 132.9],
        'sorted': [0.63, 4.20, 9.50, 29.5, 59.0, 127.0],
        'reverse': [0.68, 4.56, 10.15, 31.7, 63.4, 136.8]
    },
    'Quick Sort': {
        'random': [0.59, 3.98, 8.46, 26.5, 51.4, 113.0],
        'sorted': [0.45, 2.88, 6.20, 18.6, 40.0, 92.0],
        'reverse': [0.95, 5.95, 12.8, 39.6, 93.0, 215.0]
    },
    'Heap Sort': {
        'random': [0.79, 5.37, 11.51, 35.8, 69.3, 149.5],
        'sorted': [0.75, 5.1, 11.0, 34.0, 67.0, 145.0],
        'reverse': [0.82, 5.45, 11.75, 36.4, 70.5, 152.0]
    },
    'Counting Sort': {
        'random': [0.15, 0.75, 1.5, 3.75, 7.5, 15.0],
        'sorted': [0.15, 0.73, 1.48, 3.7, 7.4, 14.8],
        'reverse': [0.16, 0.76, 1.52, 3.8, 7.6, 15.2]
    }
}

def plot_individual_algorithm(algo_name, sizes, random_times, sorted_times, reverse_times):
    plt.figure(figsize=(10, 6))
    plt.plot(sizes, random_times, 'o-', label='Random Data', linewidth=2.5, markersize=8)
    plt.plot(sizes, sorted_times, 's-', label='Sorted Data', linewidth=2.5, markersize=8)
    plt.plot(sizes, reverse_times, '^-', label='Reverse Sorted', linewidth=2.5, markersize=8)
    
    plt.xlabel('Input Size (n)', fontsize=12, fontweight='bold')
    plt.ylabel('Time (milliseconds)', fontsize=12, fontweight='bold')
    plt.title(f'{algo_name} - Performance Analysis', fontsize=14, fontweight='bold')
    plt.legend(fontsize=10)
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    
    filename = f'{algo_name.replace(" ", "_")}_performance.png'
    plt.savefig(filename, dpi=300, bbox_inches='tight')
    print(f"✓ {filename}")
    plt.close()

def plot_all_algorithms_comparison():
    plt.figure(figsize=(14, 8))
    for algo_name, data in performance_data.items():
        plt.plot(input_sizes, data['random'], 'o-', label=algo_name, linewidth=2.5, markersize=6)
    
    plt.xlabel('Input Size (n)', fontsize=12, fontweight='bold')
    plt.ylabel('Time (milliseconds) - Log Scale', fontsize=12, fontweight='bold')
    plt.title('Sorting Algorithms - Overall Performance Comparison', fontsize=14, fontweight='bold')
    plt.yscale('log')
    plt.legend(fontsize=9, loc='upper left')
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig('comparison_all_algorithms.png', dpi=300, bbox_inches='tight')
    print("✓ comparison_all_algorithms.png")
    plt.close()

def plot_complexity_class_comparison():
    fig, axes = plt.subplots(1, 3, figsize=(18, 6))
    
    # O(n²)
    on2 = {'Bubble Sort': performance_data['Bubble Sort']['random'],
           'Selection Sort': performance_data['Selection Sort']['random'],
           'Insertion Sort': performance_data['Insertion Sort']['random']}
    for algo, times in on2.items():
        axes[0].plot(input_sizes, times, 'o-', label=algo, linewidth=2.5)
    axes[0].set_title('O(n²) Algorithms', fontweight='bold', fontsize=12)
    axes[0].set_yscale('log')
    axes[0].grid(True, alpha=0.3)
    axes[0].legend(fontsize=9)
    
    # O(n log n)
    onlogn = {'Merge Sort': performance_data['Merge Sort']['random'],
              'Quick Sort': performance_data['Quick Sort']['random'],
              'Heap Sort': performance_data['Heap Sort']['random']}
    for algo, times in onlogn.items():
        axes[1].plot(input_sizes, times, 's-', label=algo, linewidth=2.5)
    axes[1].set_title('O(n log n) Algorithms', fontweight='bold', fontsize=12)
    axes[1].grid(True, alpha=0.3)
    axes[1].legend(fontsize=9)
    
    # Linear
    linear = {'Counting Sort': performance_data['Counting Sort']['random']}
    for algo, times in linear.items():
        axes[2].plot(input_sizes, times, '^-', label=algo, linewidth=2.5, color='#2ca02c')
    axes[2].set_title('O(n + k) Algorithms', fontweight='bold', fontsize=12)
    axes[2].grid(True, alpha=0.3)
    axes[2].legend(fontsize=9)
    
    for ax in axes:
        ax.set_xlabel('Input Size (n)', fontweight='bold')
        ax.set_ylabel('Time (ms)', fontweight='bold')
    
    plt.tight_layout()
    plt.savefig('comparison_by_complexity.png', dpi=300, bbox_inches='tight')
    print("✓ comparison_by_complexity.png")
    plt.close()

def plot_bar_comparison(size=1000):
    size_idx = input_sizes.index(size)
    algo_names = list(performance_data.keys())
    times = [performance_data[algo]['random'][size_idx] for algo in algo_names]
    
    plt.figure(figsize=(12, 6))
    bars = plt.bar(range(len(algo_names)), times, color='steelblue', edgecolor='black', alpha=0.7)
    
    for bar, time in zip(bars, times):
        height = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2., height, f'{time:.2f}',
                ha='center', va='bottom', fontsize=9)
    
    plt.xticks(range(len(algo_names)), algo_names, rotation=45, ha='right')
    plt.ylabel('Time (milliseconds)', fontweight='bold')
    plt.title(f'Algorithm Performance at n={size}', fontweight='bold', fontsize=14)
    plt.grid(axis='y', alpha=0.3)
    plt.tight_layout()
    plt.savefig(f'bar_comparison_n{size}.png', dpi=300, bbox_inches='tight')
    print(f"✓ bar_comparison_n{size}.png")
    plt.close()

if __name__ == "__main__":
    print("Generating all Matplotlib visualizations...\n")
    
    print("Individual algorithm charts:")
    for algo_name, data in performance_data.items():
        plot_individual_algorithm(algo_name, input_sizes, 
                                 data['random'], data['sorted'], data['reverse'])
    
    print("\nComparison charts:")
    plot_all_algorithms_comparison()
    plot_complexity_class_comparison()
    plot_bar_comparison(1000)
    
    print("\n✓ All visualizations created successfully!")
    print("\nGenerated files:")
    print("- 7 individual algorithm charts")
    print("- 1 overall comparison chart")
    print("- 1 complexity class comparison")
    print("- 1 bar chart comparison")
```

### Run the complete script:

```bash
python generate_all_plots.py
```

---

## IMPORTANT MATPLOTLIB TIPS

### 1. Professional Styling

```python
# Use professional style
plt.style.use('seaborn-v0_8-darkgrid')

# Or try other styles:
# plt.style.use('ggplot')
# plt.style.use('bmh')
# plt.style.use('default')
```

### 2. High-Resolution Exports

```python
# Always save with high DPI for reports
plt.savefig('chart.png', dpi=300, bbox_inches='tight')

# For PDF (better for print):
plt.savefig('chart.pdf', dpi=300, bbox_inches='tight')
```

### 3. Font Sizes for Reports

```python
plt.xlabel('Input Size (n)', fontsize=12, fontweight='bold')  # Axis labels
plt.ylabel('Time (ms)', fontsize=12, fontweight='bold')
plt.title('Chart Title', fontsize=14, fontweight='bold')      # Title
plt.legend(fontsize=10)                                        # Legend
```

### 4. Log Scale (for better visualization of wide ranges)

```python
plt.yscale('log')  # Logarithmic Y-axis
# or
plt.loglog()  # Both axes logarithmic
```

### 5. Custom Colors

```python
colors = {
    'on2': '#FF6B6B',      # Red for O(n²)
    'onlogn': '#4ECDC4',   # Teal for O(n log n)
    'linear': '#51CF66'    # Green for O(n)
}

plt.plot(x, y, color=colors['onlogn'])
```

### 6. Multiple Subplots

```python
fig, axes = plt.subplots(2, 2, figsize=(14, 10))  # 2x2 grid
# axes[0,0], axes[0,1], axes[1,0], axes[1,1]
```

### 7. Adding Annotations

```python
plt.annotate('Peak Performance', xy=(5000, 100), xytext=(6000, 150),
            arrowprops=dict(arrowstyle='->', color='red'),
            fontsize=10, fontweight='bold')
```

---

## REQUIRED CHARTS FOR YOUR REPORT

Based on your DAA project requirements, create AT MINIMUM:

✓ **Chart 1:** One graph per algorithm (7 charts for 7 main algorithms)
  - X-axis: Input size
  - Y-axis: Time (ms)
  - Three lines: Random, Sorted, Reverse-sorted

✓ **Chart 2:** Overall Comparison
  - All algorithms on one graph
  - Log scale for better visualization

✓ **Chart 3:** Complexity Class Comparison
  - O(n²) algorithms together
  - O(n log n) algorithms together
  - Linear time algorithms together

✓ **Chart 4:** Bar Chart at specific size (n=1000)
  - Direct comparison of all algorithms

**TOTAL: Minimum 11 charts for comprehensive analysis**

---

## PLACING CHARTS IN YOUR REPORT

### Option A: Using PDF with Python
```python
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Image, Paragraph, PageBreak
from reportlab.lib.styles import getSampleStyleSheet

pdf = SimpleDocTemplate("report_with_charts.pdf")
elements = []

# Add text, images, etc.
elements.append(Paragraph("Results", getSampleStyleSheet()['Heading1']))
elements.append(Image('comparison_all_algorithms.png', width=500, height=350))
elements.append(PageBreak())

pdf.build(elements)
```

### Option B: Manual (Easiest for first-time)
1. Generate all PNG charts using the scripts above
2. Import them into your Word/Google Docs report
3. Add captions and labels

### Option C: LaTeX (Most Professional)
```latex
\begin{figure}[h]
  \centering
  \includegraphics[width=0.8\textwidth]{comparison_all_algorithms.png}
  \caption{Overall performance comparison of sorting algorithms}
  \label{fig:comparison}
\end{figure}
```

---

## QUICK REFERENCE: Common Issues & Solutions

| Issue | Solution |
|-------|----------|
| Chart too small/blurry | Increase DPI: `dpi=300` |
| Overlapping labels | Use `plt.xticks(rotation=45)` |
| Legend blocking data | Use `loc='upper left'` or move outside |
| Memory issues | Use `plt.close()` after each save |
| Missing imports | `pip install matplotlib numpy` |
| Files not saving | Check write permissions in directory |
| Chart looks ugly | Try `plt.style.use('seaborn-v0_8-darkgrid')` |

---

## YOUR NEXT STEPS

1. Copy one of the complete scripts above
2. Update the `performance_data` with your actual measurements
3. Run the script: `python generate_all_plots.py`
4. Verify all PNG files are created (should see 11+ files)
5. Add charts to your PDF report with captions
6. Include 2-3 lines of analysis below each chart

**Good luck with your project! 🎉**
