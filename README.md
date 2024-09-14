# Algorithm Efficiency and Scalability Analysis

This project implements and analyzes Randomized Quicksort, Deterministic Quicksort, and a Hash Table with chaining for collision resolution.

## Files

- `quickSort.py`: Implementations of Randomized and Deterministic Quicksort
- `hashTable.py`: Implementation of Hash Table with chaining
- `analysis.py`: Script to run performance tests and analysis

## How to Run

1. Ensure you have Python 3.7+ installed on your system.
2. Clone this repository or download the files to your local machine.
3. Open a terminal/command prompt and navigate to the directory containing the files.
4. Run the analysis script:
5. The script will generate an `output.txt` file in the same directory, containing the analysis results.

## Summary of Findings

### QuickSort Analysis

1. Randomized Quicksort:
- Demonstrates consistent performance across all input types (random, sorted, reverse-sorted, and repeated elements).
- Exhibits average-case time complexity of O(n log n) as expected theoretically.
- Performs well even on sorted and reverse-sorted arrays due to random pivot selection.

2. Deterministic Quicksort:
- Shows good performance on random arrays, comparable to Randomized Quicksort for smaller inputs.
- Significantly degrades in performance for sorted and reverse-sorted arrays, especially as array size increases.
- Demonstrates worst-case O(n^2) behavior for sorted/reverse-sorted inputs as predicted by theory.

3. Comparative Performance:
- Randomized Quicksort outperforms Deterministic Quicksort on sorted and reverse-sorted arrays, especially for larger sizes.
- Both algorithms perform well on arrays with repeated elements due to the implementation's handling of equal elements.

### Hash Table Analysis

1. Performance:
- Insert, search, and delete operations demonstrate average-case O(1) time complexity for reasonably sized inputs.
- Performance degrades as the load factor increases, aligning with theoretical expectations.

2. Load Factor Management:
- The implementation includes dynamic resizing to maintain a low load factor (threshold set at 0.7).
- Resizing helps in maintaining consistent performance as the number of elements grows.

3. Collision Handling:
- Chaining effectively handles collisions, allowing the hash table to accommodate more elements than its initial size.

## Conclusions

- Randomized Quicksort proves to be more robust and efficient across various input types compared to Deterministic Quicksort.
- The Hash Table implementation demonstrates efficient average-case performance for basic operations, with the resizing strategy effectively managing the load factor.
- These implementations and analyses highlight the importance of algorithm choice and implementation details in achieving efficient and scalable solutions for sorting and data storage/retrieval tasks.